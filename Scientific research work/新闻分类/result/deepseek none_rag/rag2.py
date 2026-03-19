import pandas as pd
import faiss
import numpy as np
import time
from tqdm import tqdm
from openai import OpenAI
from sentence_transformers import SentenceTransformer

# ==========================================
# 1. 配置 (已更新为 DeepSeek)
# ==========================================
API_KEY = "sk-aadf9b32e16d47ecbc4eeff3166c23fb"
BASE_URL = "https://api.deepseek.com"
MODEL_NAME = "deepseek-chat"

TRAIN_PATH = r"C:\Users\Lenovo\Desktop\code\python\data1.xlsx"
TEST_PATH  = r"C:\Users\Lenovo\Desktop\code\python\test1.xlsx"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
embedder = SentenceTransformer("all-MiniLM-L6-v2")

CATEGORIES = ["politics", "environment", "education", "world", "business", "technology", "science"]

# ==========================================
# 2. 为每个类别分别构建 RAG 索引
# ==========================================
def build_category_indices(train_df):
    indices = {}
    category_docs = {}
    for cat in CATEGORIES:
        sub_df = train_df[train_df["section"].str.lower() == cat]
        docs = sub_df["text"].fillna("").str[:300].tolist()
        emb = embedder.encode(docs, convert_to_numpy=True)
        faiss.normalize_L2(emb)
        index = faiss.IndexFlatIP(emb.shape[1])
        index.add(emb.astype("float32"))
        indices[cat] = index
        category_docs[cat] = docs
    return indices, category_docs

# ==========================================
# 3. Discriminative RAG 推理
# ==========================================
def discriminative_rag_predict(title, text, indices, category_docs, k=3):
    query = embedder.encode([title + " " + text[:200]], convert_to_numpy=True)
    faiss.normalize_L2(query)
    evidence_blocks = ""
    for cat in CATEGORIES:
        index = indices[cat]
        docs = category_docs[cat]
        _, idxs = index.search(query.astype("float32"), k)
        evidence_blocks += f"\n[{cat.upper()} EVIDENCE]\n"
        for idx in idxs[0]:
            evidence_blocks += f"- {docs[idx][:200]}\n"

    prompt = f"""You are a professional news classifier.
Based on the evidence, choose the single most appropriate category.
Categories: {CATEGORIES}
{evidence_blocks}
[Target]
Title: {title}
Snippet: {text[:300]}
Output format:
Category: <one category>
Reason: <brief explanation>"""

    try:
        resp = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=120
        )
        content = resp.choices[0].message.content.strip()
        pred, reason = "unknown", content
        for line in content.split("\n"):
            if line.lower().startswith("category:"):
                v = line.split(":", 1)[1].strip().lower()
                if v in CATEGORIES: pred = v
            elif line.lower().startswith("reason:"):
                reason = line.split(":", 1)[1].strip()
        return pred, reason
    except Exception as e:
        return "error", str(e)

def main():
    train_df = pd.read_excel(TRAIN_PATH).fillna("")
    test_df  = pd.read_excel(TEST_PATH).fillna("")
    indices, category_docs = build_category_indices(train_df)
    results, correct = [], 0

    for i in tqdm(range(len(test_df))):
        row = test_df.iloc[i]
        true_label = row["section"].strip().lower()
        pred, reason = discriminative_rag_predict(row["title"], row["text"], indices, category_docs)
        ok = int(pred == true_label)
        correct += ok
        res = row.to_dict()
        res["编号"] = i + 1
        res["预测结果"] = pred
        res["预测原因"] = reason
        res["是否正确"] = ok
        results.append(res)
        time.sleep(0.01)

    final_df = pd.DataFrame(results)
    cols = final_df.columns.tolist()
    cols.remove("编号")
    final_df = final_df[["编号"] + cols]
    sec_idx = final_df.columns.tolist().index("section") + 1
    insert_cols = ["预测结果", "预测原因", "是否正确"]
    rest = [c for c in final_df.columns if c not in insert_cols]
    final_df = final_df[rest[:sec_idx] + insert_cols + rest[sec_idx:]]

    print(f"🎯 准确率: {correct / len(test_df):.2%}")
    final_df.to_excel("Discriminative_DeepSeek_Report.xlsx", index=False)

if __name__ == "__main__":
    main()