import pandas as pd
import numpy as np
import faiss
import time
import re
from tqdm import tqdm
from openai import OpenAI
from sentence_transformers import SentenceTransformer

# ==========================================
# 1. 核心配置（已切换为 DeepSeek）
# ==========================================
# 填入你的 DeepSeek API Key
API_KEY = "sk-aadf9b32e16d47ecbc4eeff3166c23fb"
# DeepSeek 官方 API 地址
BASE_URL = "https://api.deepseek.com"
# 使用 DeepSeek V3 模型
MODEL_NAME = "deepseek-chat"

TRAIN_PATH = r"C:\Users\Lenovo\Desktop\code\python\data1.xlsx"
TEST_PATH = r"C:\Users\Lenovo\Desktop\code\python\test1.xlsx"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
# 使用标准的 MiniLM 模型进行向量化
embedder = SentenceTransformer("all-MiniLM-L6-v2")

CATEGORIES = ["politics", "environment", "education", "world", "business", "technology", "science"]

# ==========================================
# 2. 深度 RAG：构建标题+摘要的索引（原逻辑不动）
# ==========================================
def create_smart_index(train_df):
    print("🚀 正在构建深度语义索引库...")
    # 策略：标题权重加倍 + 正文首句
    train_docs = (train_df['title'] + " " + train_df['title'] + " " + train_df['text'].fillna('').str[:100]).tolist()
    embeddings = embedder.encode(train_docs, convert_to_numpy=True, show_progress_bar=False)
    
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension) 
    faiss.normalize_L2(embeddings)
    index.add(embeddings.astype('float32'))
    return index

# ==========================================
# 3. 专家级推理：调用 DeepSeek API
# ==========================================
def expert_rag_classify(title, text, index, train_df, k=6):
    # 1. 检索相似案例
    query_text = f"{title} {title} {text[:100]}"
    query_vec = embedder.encode([query_text], convert_to_numpy=True)
    faiss.normalize_L2(query_vec)
    distances, indices = index.search(query_vec.astype('float32'), k)
    
    ref_list = []
    for idx in indices[0]:
        r = train_df.iloc[idx]
        ref_list.append(f"- Title: {r['title']} -> Category: {r['section']}")
    references = "\n".join(ref_list)

    # 2. 构造专家级指令（原 Prompt 结构不动）
    prompt = f"""You are a senior news editor. Classify the news into: {CATEGORIES}.

[Reference Knowledge Base]
{references}

[Target News]
Title: {title}
Context Snippet: {text[:250]}

[Expert Classification Rules]
- 'Science' is for fundamental research (NASA, DNA, Physics).
- 'Technology' is for gadgets, apps, AI, and tech giants (Apple, Chips, Software).
- 'Politics' is for DOMESTIC government/laws.
- 'World' is for INTERNATIONAL conflicts/diplomacy.

[Task]
1. Identify the 2 most likely categories.
2. Compare the Target with the Reference cases.
3. Select the final category.

Response Format:
Reasoning: [English reasoning]
Category: [One word only]"""

    try:
        # 切换到 DeepSeek API 调用
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a precise news classification expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.01  # 极低温度确保稳定性
        )
        content = response.choices[0].message.content
        
        # 结果解析
        pred_cat = "unknown"
        for line in content.split('\n'):
            if "Category:" in line:
                val = line.split(":")[-1].strip().lower().strip('.')
                if val in CATEGORIES:
                    pred_cat = val
                    break
        
        # 兜底匹配
        if pred_cat == "unknown":
            for c in CATEGORIES:
                if c in content.lower():
                    pred_cat = c; break
                    
        return pred_cat, content
    except Exception as e:
        return "error", str(e)

# ==========================================
# 4. 主流程（原报表逻辑不动）
# ==========================================
def main():
    # 读取数据
    train_df = pd.read_excel(TRAIN_PATH)
    test_df = pd.read_excel(TEST_PATH)
    
    # 构建索引
    index = create_smart_index(train_df)
    
    results = []
    correct_count = 0
    
    print(f"📊 开始进行 DeepSeek + 深度 RAG 推理...")
    
    for i in tqdm(range(len(test_df))):
        row = test_df.iloc[i]
        true_label = str(row['section']).strip().lower()
        
        # 调用专家级分类
        pred, log = expert_rag_classify(row['title'], row['text'], index, train_df)
        
        is_correct = 1 if pred == true_label else 0
        if is_correct: correct_count += 1
        
        res_entry = row.to_dict()
        res_entry['编号'] = i + 1
        res_entry['预测结果'] = pred
        res_entry['模型推理过程'] = log
        res_entry['是否正确'] = is_correct
        results.append(res_entry)
        
        # 保护性短延时
        time.sleep(0.01)

    final_df = pd.DataFrame(results)
    
    # 调整列顺序
    cols = list(test_df.columns)
    sec_idx = cols.index('section') + 1
    new_cols = ['编号'] + cols[:sec_idx] + ['预测结果', '模型推理过程', '是否正确'] + cols[sec_idx:]
    final_df = final_df[list(dict.fromkeys(new_cols))]

    # 计算最终准确率
    accuracy = correct_count / len(test_df)
    print(f"\n🎯 DeepSeek RAG 最终准确率: {accuracy:.2%}")
    
    output_file = "DeepSeek_Expert_RAG_Report.xlsx"
    final_df.to_excel(output_file, index=False)
    print(f"✅ 报表已生成：{output_file}")

if __name__ == "__main__":
    main()