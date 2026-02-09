import pandas as pd
import numpy as np
import faiss
import time
import re
from tqdm import tqdm
from openai import OpenAI
from sentence_transformers import SentenceTransformer

# ==========================================
# 1. 核心配置 (已切换至 DeepSeek)
# ==========================================
# 使用你提供的 DeepSeek Key
API_KEY = "sk-aadf9b32e16d47ecbc4eeff3166c23fb"
# DeepSeek 官方 API 终结点
BASE_URL = "https://api.deepseek.com"
# 使用 DeepSeek V3 模型
MODEL_NAME = "deepseek-chat"

TRAIN_PATH = r"C:\Users\Lenovo\Desktop\code\python\data1.xlsx"
TEST_PATH = r"C:\Users\Lenovo\Desktop\code\python\test1.xlsx"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
# 使用标准的 MiniLM 模型进行向量化，兼顾速度与精度
embedder = SentenceTransformer("all-MiniLM-L6-v2")

CATEGORIES = ["politics", "environment", "education", "world", "business", "technology", "science"]

# ==========================================
# 2. 标准 RAG：构建向量空间索引 (保持原逻辑)
# ==========================================
def create_rag_index(train_df):
    print("🚀 正在构建标准 RAG 语义索引...")
    # 结合标题和正文前150字，形成强语义特征
    train_docs = (train_df['title'] + " " + train_df['text'].fillna('').str[:150]).tolist()
    embeddings = embedder.encode(train_docs, convert_to_numpy=True, show_progress_bar=False)
    
    # 使用 FAISS 规范化向量并建立索引
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension) # 使用内积（余弦相似度）
    faiss.normalize_L2(embeddings)
    index.add(embeddings.astype('float32'))
    return index

# ==========================================
# 3. 高精度推理函数 (DeepSeek API 适配)
# ==========================================
def high_precision_predict(title, text, index, train_df, k=5):
    # --- Retrieval (检索) ---
    query_text = f"{title} {text[:150]}"
    query_vec = embedder.encode([query_text], convert_to_numpy=True)
    faiss.normalize_L2(query_vec)
    distances, indices = index.search(query_vec.astype('float32'), k)
    
    # --- Augmentation (增强) ---
    # 获取 5 个最相关的真实案例
    references = ""
    for idx in indices[0]:
        ref_row = train_df.iloc[idx]
        references += f"Reference News: {ref_row['title']}\nCorrect Category: {ref_row['section']}\n\n"

    # --- Generation (生成) ---
    # 保持原 Prompt 结构不动
    prompt = f"""You are an expert news classifier. Classify the following news item into one of these categories: {CATEGORIES}.

[Contextual Examples from Knowledge Base]
{references}

[Target News]
Title: {title}
Snippet: {text[:400]}

Instruction:
1. Compare the target news with the reference examples.
2. Provide a brief reasoning in English about why it belongs to a specific category.
3. Output the exact category name.

Response Format:
Reasoning: [English reasoning]
Category: [Exact category name]
"""

    try:
        # 调用 DeepSeek API
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that classifies news accurately."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1 # 保持低温度确保分类一致性
        )
        content = response.choices[0].message.content
        
        # 使用正则提取类别，保持原解析逻辑
        cat_match = re.search(r"Category:\s*(\w+)", content, re.IGNORECASE)
        pred_cat = cat_match.group(1).lower() if cat_match else "unknown"
        
        if pred_cat not in CATEGORIES:
            # 兜底：关键词匹配
            for c in CATEGORIES:
                if c in content.lower():
                    pred_cat = c
                    break
        
        return pred_cat, content
    except Exception as e:
        return "error", str(e)

# ==========================================
# 4. 执行主程序并输出报表 (保持原逻辑)
# ==========================================
def main():
    print("1️⃣ 加载数据...")
    train_df = pd.read_excel(TRAIN_PATH)
    test_df = pd.read_excel(TEST_PATH)
    
    # 构建 RAG 核心
    index = create_rag_index(train_df)
    
    results = []
    correct_count = 0
    
    print(f"2️⃣ 开始 DeepSeek RAG 分类（共 {len(test_df)} 条）...")
    for i in tqdm(range(len(test_df))):
        row = test_df.iloc[i]
        true_label = str(row['section']).strip().lower()
        
        # 执行预测
        pred, model_output = high_precision_predict(row['title'], row['text'], index, train_df)
        
        # 统计
        is_correct = 1 if pred == true_label else 0
        if is_correct: correct_count += 1
        
        # 记录结果
        res_entry = row.to_dict()
        res_entry['编号'] = i + 1
        res_entry['预测结果'] = pred
        res_entry['模型推理过程'] = model_output
        res_entry['是否正确'] = is_correct
        results.append(res_entry)
        
        # 稍微增加一点停顿，确保 API 调用频率稳定
        time.sleep(0.01)

    # 3️⃣ 生成报表
    final_df = pd.DataFrame(results)
    
    # 调整列顺序
    orig_cols = list(test_df.columns)
    sec_idx = orig_cols.index('section') + 1
    new_order = ['编号'] + orig_cols[:sec_idx] + ['预测结果', '模型推理过程', '是否正确'] + orig_cols[sec_idx:]
    final_df = final_df[list(dict.fromkeys(new_order))]

    accuracy = correct_count / len(test_df)
    print(f"\n🎯 最终 DeepSeek RAG 预测准确率: {accuracy:.2%}")
    
    output_file = "DeepSeek_High_Precision_RAG_Report.xlsx"
    final_df.to_excel(output_file, index=False)
    print(f"✅ 结果已保存至: {output_file}")

if __name__ == "__main__":
    main()