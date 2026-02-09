import pandas as pd
import numpy as np
import faiss
import time
import re
from tqdm import tqdm
from openai import OpenAI
from sentence_transformers import SentenceTransformer

# ==========================================
# 1. 核心配置
# ==========================================
API_KEY = "sk-5bdab01fc4fd493fa2ccc854d74420ed"
BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
MODEL_NAME = "qwen-turbo"

TRAIN_PATH = r"C:\Users\Lenovo\Desktop\code\python\data1.xlsx"
TEST_PATH = r"C:\Users\Lenovo\Desktop\code\python\test1.xlsx"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
embedder = SentenceTransformer("all-MiniLM-L6-v2")

CATEGORIES = ["politics", "environment", "education", "world", "business", "technology", "science"]

# ==========================================
# 2. RAG 索引构建
# ==========================================
def create_rag_index(train_df):
    print("🚀 正在构建标准 RAG 语义索引...")
    train_docs = (train_df['title'] + " " + train_df['text'].fillna('').str[:150]).tolist()
    embeddings = embedder.encode(train_docs, convert_to_numpy=True, show_progress_bar=False)
    
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)
    faiss.normalize_L2(embeddings)
    index.add(embeddings.astype('float32'))
    return index

# ==========================================
# 3. 标准 RAG + CoT 推理函数
# ==========================================
def high_precision_predict_cot(title, text, index, train_df, k=5):
    # --- 检索相似案例 ---
    query_text = f"{title} {text[:150]}"
    query_vec = embedder.encode([query_text], convert_to_numpy=True)
    faiss.normalize_L2(query_vec)
    distances, indices = index.search(query_vec.astype('float32'), k)
    
    references = ""
    for idx in indices[0]:
        ref_row = train_df.iloc[idx]
        references += f"- Ref: {ref_row['title']} | Category: {ref_row['section']}\n"

    # --- 构造思维链 Prompt ---
    prompt = f"""You are an expert news analyst. Classify the Target News using the provided Knowledge Base.

[Knowledge Base]
{references}

[Target News]
Title: {title}
Snippet: {text[:400]}

[Instruction]
1. Compare the Target News with the Reference examples in the Knowledge Base.
2. Identify shared keywords or thematic similarities.
3. Reason step-by-step why it fits a specific category.
4. Output the Reasoning first, then the final Category.

Response Format:
Reasoning: [English reasoning]
Category: [Exact category name from the list]
"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=300
        )
        content = response.choices[0].message.content
        
        # 精准解析
        cat_match = re.search(r"Category:\s*(\w+)", content, re.IGNORECASE)
        pred_cat = cat_match.group(1).lower() if cat_match else "unknown"
        
        if pred_cat not in CATEGORIES:
            for c in CATEGORIES:
                if c in content.lower().split("category:")[-1]:
                    pred_cat = c; break
        
        return pred_cat, content
    except Exception as e:
        return "error", str(e)

# ==========================================
# 4. 主流程
# ==========================================
def main():
    train_df = pd.read_excel(TRAIN_PATH)
    test_df = pd.read_excel(TEST_PATH)
    index = create_rag_index(train_df)
    
    results = []
    correct_count = 0
    
    print(f"📊 正在执行标准 RAG + CoT...")
    for i in tqdm(range(len(test_df))):
        row = test_df.iloc[i]
        true_label = str(row['section']).strip().lower()
        pred, log = high_precision_predict_cot(row['title'], row['text'], index, train_df)
        
        is_correct = 1 if pred == true_label else 0
        if is_correct: correct_count += 1
        
        res_entry = row.to_dict()
        res_entry['编号'] = i + 1
        res_entry['预测结果'] = pred
        res_entry['推理过程'] = log
        res_entry['是否正确'] = is_correct
        results.append(res_entry)
        time.sleep(0.01)

    final_df = pd.DataFrame(results)
    print(f"\n🎯 最终准确率: {correct_count / len(test_df):.2%}")
    final_df.to_excel("Standard_RAG_CoT_Report.xlsx", index=False)

if __name__ == "__main__":
    main()