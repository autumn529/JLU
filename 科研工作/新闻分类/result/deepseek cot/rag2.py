import pandas as pd
import numpy as np
import faiss
import time
import re
from tqdm import tqdm
from openai import OpenAI
from sentence_transformers import SentenceTransformer

# ==========================================
# 1. 核心配置 (DeepSeek Expert CoT RAG)
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
# 2. 深度 RAG：构建标题权重增强索引
# ==========================================
def create_smart_index(train_df):
    print("🚀 正在构建深度语义索引库...")
    # 策略：标题重复两次以增加检索权重
    train_docs = (train_df['title'] + " " + train_df['title'] + " " + train_df['text'].fillna('').str[:100]).tolist()
    embeddings = embedder.encode(train_docs, convert_to_numpy=True, show_progress_bar=False)
    
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension) 
    faiss.normalize_L2(embeddings)
    index.add(embeddings.astype('float32'))
    return index

# ==========================================
# 3. 专家级思维链推理函数
# ==========================================
def expert_rag_classify_cot(title, text, index, train_df, k=6):
    # --- 1. 语义检索 ---
    query_text = f"{title} {title} {text[:100]}"
    query_vec = embedder.encode([query_text], convert_to_numpy=True)
    faiss.normalize_L2(query_vec)
    distances, indices = index.search(query_vec.astype('float32'), k)
    
    ref_list = []
    for idx in indices[0]:
        r = train_df.iloc[idx]
        ref_list.append(f"- Reference: {r['title']} | Category: {r['section']}")
    references = "\n".join(ref_list)

    # --- 2. 构造 CoT 专家指令 ---
    prompt = f"""You are a senior news editor. Analyze and classify the [Target News] based on rules and references.

[Expert Rules]
- 'Science': Fundamental research, discovery, space, biology (e.g., NASA, DNA, Physics).
- 'Technology': Applied science, gadgets, AI, tech companies, software/hardware.
- 'Politics': DOMESTIC government, elections, policy, and legislation.
- 'World': INTERNATIONAL relations, conflicts, and global diplomacy.

[Reference Knowledge Base]
{references}

[Target News]
Title: {title}
Context: {text[:300]}

[Task: Chain of Thought]
1. Subject Analysis: Identify the core entity and action in the target news.
2. Reference Comparison: Compare the target news with the reference cases above.
3. Category Elimination: Explain why it fits one category better than the most similar alternative.
4. Final Decision: Provide the final category name.

Response Format:
Reasoning: [Your step-by-step analysis]
Category: [Exact category name from the list]
"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a precise news analyst. Use structured logical reasoning to classify items."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.01, # 极低随机性
            max_tokens=400   # 留够空间给推理过程
        )
        content = response.choices[0].message.content
        
        # --- 3. 强力解析逻辑 ---
        pred_cat = "unknown"
        # 寻找最后一行的 Category: 标记
        cat_match = re.search(r"Category:\s*(\w+)", content, re.IGNORECASE)
        if cat_match:
            val = cat_match.group(1).lower().strip()
            if val in CATEGORIES:
                pred_cat = val
        
        # 兜底：如果正则没抓到，全文匹配
        if pred_cat == "unknown":
            search_text = content.lower().split("category:")[-1]
            for c in CATEGORIES:
                if c in search_text:
                    pred_cat = c
                    break
                    
        return pred_cat, content
    except Exception as e:
        return "error", str(e)

# ==========================================
# 4. 主程序
# ==========================================
def main():
    print("1️⃣ 加载本地数据...")
    train_df = pd.read_excel(TRAIN_PATH)
    test_df = pd.read_excel(TEST_PATH)
    
    index = create_smart_index(train_df)
    
    results = []
    correct_count = 0
    
    print(f"2️⃣ 启动 DeepSeek Expert RAG + CoT 推理（共 {len(test_df)} 条）...")
    
    for i in tqdm(range(len(test_df))):
        row = test_df.iloc[i]
        true_label = str(row['section']).strip().lower()
        
        # 调用改进后的 CoT 推理
        pred, log = expert_rag_classify_cot(row['title'], row['text'], index, train_df)
        
        is_correct = 1 if pred == true_label else 0
        if is_correct: correct_count += 1
        
        # 封装数据
        res_entry = row.to_dict()
        res_entry['编号'] = i + 1
        res_entry['预测结果'] = pred
        res_entry['思维链过程 (CoT)'] = log
        res_entry['是否正确'] = is_correct
        results.append(res_entry)
        
        time.sleep(0.01)

    # 3️⃣ 结果导出
    final_df = pd.DataFrame(results)
    
    # 动态重排序列，把结果列插在 section 后面
    cols = list(test_df.columns)
    sec_idx = cols.index('section') + 1
    new_cols = ['编号'] + cols[:sec_idx] + ['预测结果', '思维链过程 (CoT)', '是否正确'] + cols[sec_idx:]
    final_df = final_df[list(dict.fromkeys(new_cols))]

    accuracy = correct_count / len(test_df)
    print(f"\n🎯 DeepSeek Expert CoT 最终准确率: {accuracy:.2%}")
    
    output_file = "DeepSeek_Expert_CoT_RAG_Report.xlsx"
    final_df.to_excel(output_file, index=False)
    print(f"✅ 详细报表已生成：{output_file}")

if __name__ == "__main__":
    main()