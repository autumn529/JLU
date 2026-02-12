import pandas as pd
import faiss
import numpy as np
import time
from tqdm import tqdm
from openai import OpenAI
from sentence_transformers import SentenceTransformer

# ==========================================
# 1. 配置
# ==========================================
API_KEY = "sk-5bdab01fc4fd493fa2ccc854d74420ed"
BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
MODEL_NAME = "qwen-turbo"

TRAIN_PATH = r"C:\Users\Lenovo\Desktop\code\python\data1.xlsx"
TEST_PATH  = r"C:\Users\Lenovo\Desktop\code\python\test1.xlsx"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
embedder = SentenceTransformer("all-MiniLM-L6-v2")

CATEGORIES = ["politics", "environment", "education", "world", "business", "technology", "science"]

# ==========================================
# 2. 为每个类别分别构建 RAG 索引（核心差异点）
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
# 3. 判别式 RAG + 隐式 CoT（不输出 Thought）
# ==========================================
def discriminative_rag_cot_predict(title, text, indices, category_docs, k=3):
    query = embedder.encode([title + " " + text[:200]], convert_to_numpy=True)
    faiss.normalize_L2(query)

    evidence_blocks = ""

    for cat in CATEGORIES:
        index = indices[cat]
        docs  = category_docs[cat]

        _, idxs = index.search(query.astype("float32"), k)

        evidence_blocks += f"\n[{cat.upper()} EVIDENCE]\n"
        for idx in idxs[0]:
            evidence_blocks += f"- {docs[idx][:200]}\n"

    prompt = f"""
You are a professional news classifier.

You are given evidence retrieved separately for each category.
Carefully reason internally which category is best supported.
Do NOT reveal your reasoning.

Categories: {CATEGORIES}

{evidence_blocks}

[Target]
Title: {title}
Snippet: {text[:300]}

Output format:
Category: <one category>
Reason: <short justification>
"""

    try:
        resp = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=120
        )

        content = resp.choices[0].message.content.strip()

        pred = "unknown"
        reason = content

        for line in content.split("\n"):
            if line.lower().startswith("category:"):
                v = line.split(":", 1)[1].strip().lower()
                if v in CATEGORIES:
                    pred = v
            elif line.lower().startswith("reason:"):
                reason = line.split(":", 1)[1].strip()

        return pred, reason

    except Exception as e:
        return "error", str(e)

# ==========================================
# 4. 主程序（文档输出格式保持一致）
# ==========================================
def main():
    train_df = pd.read_excel(TRAIN_PATH).fillna("")
    test_df  = pd.read_excel(TEST_PATH).fillna("")

    indices, category_docs = build_category_indices(train_df)

    results = []
    correct = 0

    for i in tqdm(range(len(test_df))):
        row = test_df.iloc[i]
        true_label = row["section"].strip().lower()

        pred, reason = discriminative_rag_cot_predict(
            row["title"], row["text"], indices, category_docs
        )

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

    # 编号放第一列
    cols = final_df.columns.tolist()
    cols.remove("编号")
    final_df = final_df[["编号"] + cols]

    # section 后插入三列
    cols = final_df.columns.tolist()
    sec_idx = cols.index("section") + 1
    insert_cols = ["预测结果", "预测原因", "是否正确"]
    rest = [c for c in cols if c not in insert_cols]

    final_df = final_df[
        rest[:sec_idx] + insert_cols + rest[sec_idx:]
    ]

    acc = correct / len(test_df)
    print(f"🎯 Discriminative RAG + CoT 准确率: {acc:.2%}")

    final_df.to_excel("Discriminative_RAG_CoT_Report.xlsx", index=False)

if __name__ == "__main__":
    main()
