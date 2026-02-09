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
# 2. 深度检索：标题权重翻倍
# ==========================================
def create_smart_index(train_df):
    print("🚀 正在构建深度语义索引库...")
    # 策略：通过重复标题增强其检索权重
    train_docs = (train_df['title'] + " " + train_df['title'] + " " + train_df['text'].fillna('').str[:100]).tolist()
    embeddings = embedder.encode(train_docs, convert_to_numpy=True, show_progress_bar=False)
    
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension) 
    faiss.normalize_L2(embeddings)
    index.add(embeddings.astype('float32'))
    return index

# ==========================================
# 3. 专家级思维链推理
# ==========================================
def expert_rag_classify_cot(title, text, index, train_df, k=6):
    # --- 检索 ---
    query_text = f"{title} {title} {text[:100]}"
    query_vec = embedder.encode([query_text], convert_to_numpy=True)
    faiss.normalize_L2(query_vec)
    distances, indices = index.search(query_vec.astype('float32'), k)
    
    ref_list = [f"- {train_df.iloc[idx]['title']} -> {train_df.iloc[idx]['section']}" for idx in indices[0]]
    references = "\n".join(ref_list)

    # --- 构造专家级 CoT 指令 ---
    prompt = f"""You are a senior news editor. Task: Classify the [Target] into: {CATEGORIES}.

[Classification Rules]
- 'Science': Focus on research, nature, physics, or space discovery.
- 'Technology': Focus on gadgets, digital software, AI, or tech corporations.
- 'Politics': Domestic policy, government decisions, or elections.
- 'World': International affairs, diplomacy, or cross-border conflicts.

[References from Knowledge Base]
{references}

[Target News]
Title: {title}
Snippet: {text[:250]}

[Expert Thinking Path]
1. Keyword Extraction: Identify main entities and actions.
2. Similarity Check: Which Reference case matches best?
3. Elimination: Why is it NOT the 2nd most likely category?
4. Final Conclusion.

Response Format:
Reasoning: [Structured analysis]
Category: [One word only]
"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.01,
            max_tokens=400
        )
        content = response.choices[0].message.content
        
        # 稳健解析
        cat_match = re.search(r"Category:\s*(\w+)", content, re.IGNORECASE)
        pred_cat = cat_match.group(1).lower().strip().replace(".", "")
        
        if pred_cat not in CATEGORIES:
            search_area = content.lower().split("category:")[-1]
            for c in CATEGORIES:
                if c in search_area:
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
    index = create_smart_index(train_df)
    
    results = []
    correct_count = 0
    print(f"📊 正在执行专家级 RAG + CoT（追求 85%+ 准确率）...")
    
    for i in tqdm(range(len(test_df))):
        row = test_df.iloc[i]
        true_label = str(row['section']).strip().lower()
        pred, log = expert_rag_classify_cot(row['title'], row['text'], index, train_df)
        
        is_correct = 1 if pred == true_label else 0
        if is_correct: correct_count += 1
        
        res_entry = row.to_dict()
        res_entry['编号'] = i + 1
        res_entry['预测结果'] = pred
        res_entry['专家推理过程'] = log
        res_entry['是否正确'] = is_correct
        results.append(res_entry)
        time.sleep(0.01)

    final_df = pd.DataFrame(results)
    print(f"\n🎯 最终准确率: {correct_count / len(test_df):.2%}")
    final_df.to_excel("Expert_RAG_CoT_Report.xlsx", index=False)

if __name__ == "__main__":
    main()