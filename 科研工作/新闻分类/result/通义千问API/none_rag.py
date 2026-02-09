import pandas as pd
import time
from tqdm import tqdm
from openai import OpenAI

# ==========================================
# 1. 基础配置
# ==========================================
API_KEY = "sk-5bdab01fc4fd493fa2ccc854d74420ed"
BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
MODEL_NAME = "qwen-turbo"

# 只保留测试集路径，不加载 data1
TEST_PATH = r"C:\Users\Lenovo\Desktop\code\python\test1.xlsx"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
CATEGORIES = ["politics", "environment", "education", "world", "business", "technology", "science"]

# ==========================================
# 2. 纯零样本预测逻辑 (Zero-shot)
# ==========================================
def zero_shot_predict(title):
    """
    完全不参考训练集，只给一个标题让模型硬猜。
    """
    prompt = f"Classify this news title into one of: {CATEGORIES}.\nTitle: {title}\nCategory:"

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,  # 保持确定性
            max_tokens=10
        )
        content = response.choices[0].message.content.strip().lower().replace(".", "")
        
        # 简单结果清洗
        pred_cat = "unknown"
        for c in CATEGORIES:
            if c in content:
                pred_cat = c
                break
        return pred_cat, content
    except Exception as e:
        return "error", str(e)

# ==========================================
# 3. 主程序
# ==========================================
def main():
    # 1. 直接加载测试集
    print(f"🚀 正在加载测试数据: {TEST_PATH}")
    test_df = pd.read_excel(TEST_PATH)
    
    results = []
    correct_count = 0
    
    print(f"📊 开始‘零样本’纯模型推理（共 {len(test_df)} 条）...")
    
    for i in tqdm(range(len(test_df))):
        row = test_df.iloc[i]
        true_label = str(row['section']).strip().lower()
        
        # 只传标题，不传正文，也不传任何学习样本
        pred, raw_out = zero_shot_predict(row['title'])
        
        # 统计
        is_correct = 1 if pred == true_label else 0
        if is_correct: correct_count += 1
        
        # 记录
        res_data = row.to_dict()
        res_data['编号'] = i + 1
        res_data['预测结果'] = pred
        res_data['是否正确'] = is_correct
        results.append(res_data)
        
        # 极短停顿
        time.sleep(0.01)

    # 2. 生成结果报表
    final_df = pd.DataFrame(results)
    accuracy = correct_count / len(test_df)
    
    print(f"\n🎯 纯模型 Zero-shot 准确率: {accuracy:.2%}")
    
    output_name = "Zero_Shot_50_Accuracy_Results.xlsx"
    final_df.to_excel(output_name, index=False)
    print(f"✅ 结果已保存至: {output_name}")

if __name__ == "__main__":
    main()