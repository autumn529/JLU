import pandas as pd
import time
import re
from tqdm import tqdm
from openai import OpenAI

# ==========================================
# 1. 基础配置
# ==========================================
API_KEY = "sk-5bdab01fc4fd493fa2ccc854d74420ed"
BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
MODEL_NAME = "qwen-turbo"

TEST_PATH = r"C:\Users\Lenovo\Desktop\code\python\test1.xlsx"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
CATEGORIES = ["politics", "environment", "education", "world", "business", "technology", "science"]

# ==========================================
# 2. 零样本思维链逻辑
# ==========================================
def zero_shot_cot_predict(title):
    # 引导模型执行思维链
    prompt = f"""Task: Classify the news title into one of: {CATEGORIES}.

Title: {title}

Instruction:
1. Analyze the core keywords and subject of the title.
2. Reason step-by-step which category it logically belongs to.
3. Output your reasoning and then the final category name.

Response Format:
Reasoning: [Brief analysis]
Category: [Exact category name]"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=200 # 扩展示理空间
        )
        content = response.choices[0].message.content
        
        # 使用正则精准提取
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
# 3. 主程序 (保持原报表逻辑)
# ==========================================
def main():
    test_df = pd.read_excel(TEST_PATH)
    results = []
    correct_count = 0
    print(f"📊 开始‘零样本 CoT’推理（共 {len(test_df)} 条）...")
    
    for i in tqdm(range(len(test_df))):
        row = test_df.iloc[i]
        true_label = str(row['section']).strip().lower()
        pred, full_log = zero_shot_cot_predict(row['title'])
        
        is_correct = 1 if pred == true_label else 0
        if is_correct: correct_count += 1
        
        res_data = row.to_dict()
        res_data['编号'] = i + 1
        res_data['预测结果'] = pred
        res_data['推理过程'] = full_log
        res_data['是否正确'] = is_correct
        results.append(res_data)
        time.sleep(0.01)

    final_df = pd.DataFrame(results)
    print(f"\n🎯 准确率: {correct_count / len(test_df):.2%}")
    final_df.to_excel("Zero_Shot_CoT_Results.xlsx", index=False)

if __name__ == "__main__":
    main()