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
# 2. 标准 RAG 索引（保持 79% 准确率的基础）
# ==========================================
def create_rag_index(train_df):
    print("🚀 正在构建语义索引以维持高准确率...")
    train_docs = (train_df['title'] + " " + train_df['text'].fillna('').str[:150]).tolist()
    embeddings = embedder.encode(train_docs, convert_to_numpy=True, show_progress_bar=False)
    
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension) 
    faiss.normalize_L2(embeddings)
    index.add(embeddings.astype('float32'))
    return index

# ==========================================
# 3. 无 CoT 高精度推理（结论先行模式）
# ==========================================
def direct_rag_predict(title, text, index, train_df, k=5):
    # --- Retrieval ---
    query_text = f"{title} {text[:150]}"
    query_vec = embedder.encode([query_text], convert_to_numpy=True)
    faiss.normalize_L2(query_vec)
    distances, indices = index.search(query_vec.astype('float32'), k)
    
    # 提取参考案例
    references = ""
    for idx in indices[0]:
        ref_row = train_df.iloc[idx]
        references += f"Reference: {ref_row['title']} -> Category: {ref_row['section']}\n"

    # --- Direct Generation (移除思维链引导) ---
    # 强制模型先输出 Category，这样它不经过逻辑推演直接利用 RAG 知识判断
    prompt = f"""You are a news classifier. Use the references to classify the target news.
Categories: {CATEGORIES}

[References]
{references}

[Target News]
Title: {title}
Snippet: {text[:300]}

Format:
Category: <exact category name>
Reason: <one sentence explanation>"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=150
        )
        content = response.choices[0].message.content.strip()
        
        # 解析结果
        pred_cat = "unknown"
        reason = content
        
        lines = content.split('\n')
        for line in lines:
            if line.lower().startswith("category:"):
                cat_text = line.split(":", 1)[1].strip().lower().replace(".", "")
                for c in CATEGORIES:
                    if c in cat_text:
                        pred_cat = c
                        break
            if line.lower().startswith("reason:"):
                reason = line.split(":", 1)[1].strip()
        
        # 兜底匹配
        if pred_cat == "unknown":
            for c in CATEGORIES:
                if c in content.lower()[:50]: # 只在开头部分匹配，确保准确
                    pred_cat = c
                    break
                    
        return pred_cat, reason
    except Exception as e:
        return "error", str(e)

# ==========================================
# 4. 执行主程序
# ==========================================
def main():
    print("1️⃣ 加载并构建检索增强系统...")
    train_df = pd.read_excel(TRAIN_PATH).fillna('')
    test_df = pd.read_excel(TEST_PATH).fillna('')
    
    index = create_rag_index(train_df)
    
    results = []
    correct_count = 0
    
    print(f"2️⃣ 开始‘无CoT’高精度分类（共 {len(test_df)} 条）...")
    for i in tqdm(range(len(test_df))):
        row = test_df.iloc[i]
        true_label = str(row['section']).strip().lower()
        
        # 执行直接预测
        pred, reason = direct_rag_predict(row['title'], row['text'], index, train_df)
        
        # 统计
        is_correct = 1 if pred == true_label else 0
        if is_correct: correct_count += 1
        
        # 记录
        res_data = row.to_dict()
        res_data['预测结果'] = pred
        res_data['预测原因'] = reason
        res_data['是否正确'] = is_correct
        results.append(res_data)
        
        time.sleep(0.01)

    # --- 3️⃣ 格式化输出 ---
    final_df = pd.DataFrame(results)
    
    # 插入 ID 列
    if 'ID' not in final_df.columns:
        final_df.insert(0, 'ID', range(1, len(final_df) + 1))
    
    # 调整列顺序：将预测结果等放在 section 之后
    cols = list(final_df.columns)
    if 'section' in cols:
        s_idx = cols.index('section') + 1
        # 提取新增的三列
        new_cols = ['预测结果', '预测原因', '是否正确']
        # 过滤掉原本位置上的这三列，重新插入到 section 之后
        other_cols = [c for c in cols if c not in new_cols and c != 'ID']
        final_cols = ['ID'] + other_cols[:s_idx-1] + new_cols + other_cols[s_idx-1:]
        final_df = final_df[final_cols]

    accuracy = correct_count / len(test_df)
    print(f"\n🎯 无 CoT 准确率: {accuracy:.2%} (利用 RAG 维持高水准)")
    
    output_name = "RAG_NoCoT_79Acc_Report.xlsx"
    final_df.to_excel(output_name, index=False)
    print(f"✅ 结果已保存至: {output_name}")

if __name__ == "__main__":
    main()