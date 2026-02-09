import pandas as pd
import numpy as np
import faiss
import time
import re
from tqdm import tqdm
from openai import OpenAI
from sentence_transformers import SentenceTransformer

# ==========================================
# 1. 核心配置 (DeepSeek CoT RAG 版)
# ==========================================
API_KEY = "sk-aadf9b32e16d47ecbc4eeff3166c23fb"
BASE_URL = "https://api.deepseek.com"
MODEL_NAME = "deepseek-chat"

TRAIN_PATH = r"C:\Users\Lenovo\Desktop\code\python\data1.xlsx"
TEST_PATH = r"C:\Users\Lenovo\Desktop\code\python\test1.xlsx"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
embedder = SentenceTransformer("all-MiniLM-L6-v2")

CATEGORIES = ["politics", "environment", "education", "world", "business", "technology", "science"]

# ==========================================
# 2. 标准 RAG：构建向量空间索引
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
# 3. 思维链推理函数 (RAG + CoT)
# ==========================================
def high_precision_predict_cot(title, text, index, train_df, k=5):
    # --- Retrieval (检索) ---
    query_text = f"{title} {text[:150]}"
    query_vec = embedder.encode([query_text], convert_to_numpy=True)
    faiss.normalize_L2(query_vec)
    distances, indices = index.search(query_vec.astype('float32'), k)
    
    # --- Augmentation (增强) ---
    references = ""
    for idx in indices[0]:
        ref_row = train_df.iloc[idx]
        references += f"- Reference Title: {ref_row['title']}\n  Correct Category: {ref_row['section']}\n\n"

    # --- Generation (思维链 Prompt) ---
    prompt = f"""You are an expert news analyst. Your task is to classify the [Target News] into one of these categories: {CATEGORIES}.

[Contextual Examples from Knowledge Base]
{references}

[Target News]
Title: {title}
Snippet: {text[:400]}

Instruction:
1. Analyze the keywords and subject of the [Target News].
2. Compare the target news with the provided [Contextual Examples].
3. Step-by-step, reason why it belongs to a specific category and why other similar categories might be incorrect.
4. Output the reasoning first, followed by the exact category.

Response Format:
Reasoning: <Your logical step-by-step analysis>
Category: <Exact category name only>
"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a professional news classifier that uses logical reasoning."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,  # 保持确定性
            max_tokens=300    # 增加 token 限制以容纳推理逻辑
        )
        content = response.choices[0].message.content
        
        # 结果解析：提取 Category 后的内容
        cat_match = re.search(r"Category:\s*(\w+)", content, re.IGNORECASE)
        pred_cat = cat_match.group(1).lower() if cat_match else "unknown"
        
        # 兜底匹配
        if pred_cat not in CATEGORIES:
            for c in CATEGORIES:
                if c in content.lower().split('category:')[-1]:
                    pred_cat = c
                    break
        
        return pred_cat, content
    except Exception as e:
        return "error", str(e)

# ==========================================
# 4. 执行主程序
# ==========================================
def main():
    print("1️⃣ 加载数据...")
    train_df = pd.read_excel(TRAIN_PATH)
    test_df = pd.read_excel(TEST_PATH)
    
    index = create_rag_index(train_df)
    
    results = []
    correct_count = 0
    
    print(f"2️⃣ 开始 DeepSeek RAG + CoT 分类（共 {len(test_df)} 条）...")
    for i in tqdm(range(len(test_df))):
        row = test_df.iloc[i]
        true_label = str(row['section']).strip().lower()
        
        # 使用思维链预测
        pred, model_output = high_precision_predict_cot(row['title'], row['text'], index, train_df)
        
        is_correct = 1 if pred == true_label else 0
        if is_correct: correct_count += 1
        
        res_entry = row.to_dict()
        res_entry['编号'] = i + 1
        res_entry['预测结果'] = pred
        res_entry['模型推理过程 (CoT)'] = model_output
        res_entry['是否正确'] = is_correct
        results.append(res_entry)
        
        time.sleep(0.01)

    # 3️⃣ 生成报表
    final_df = pd.DataFrame(results)
    
    orig_cols = list(test_df.columns)
    sec_idx = orig_cols.index('section') + 1
    new_order = ['编号'] + orig_cols[:sec_idx] + ['预测结果', '模型推理过程 (CoT)', '是否正确'] + orig_cols[sec_idx:]
    final_df = final_df[list(dict.fromkeys(new_order))]

    accuracy = correct_count / len(test_df)
    print(f"\n🎯 DeepSeek RAG+CoT 最终准确率: {accuracy:.2%}")
    
    output_file = "DeepSeek_RAG_CoT_Report.xlsx"
    final_df.to_excel(output_file, index=False)
    print(f"✅ 结果已保存至: {output_file}")

if __name__ == "__main__":
    main()