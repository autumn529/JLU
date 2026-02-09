import pandas as pd
import time
from tqdm import tqdm
from openai import OpenAI

# ==========================================
# 1. 基础配置（已改为 DeepSeek API）
# ==========================================
# 你的 DeepSeek API Key
API_KEY = "sk-aadf9b32e16d47ecbc4eeff3166c23fb"
# DeepSeek 标准 API 地址
BASE_URL = "https://api.deepseek.com"
# 使用 DeepSeek V3 模型 (deepseek-chat)
MODEL_NAME = "deepseek-chat"

# 测试集路径
TEST_PATH = r"C:\Users\Lenovo\Desktop\code\python\test1.xlsx"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
CATEGORIES = ["politics", "environment", "education", "world", "business", "technology", "science"]

# ==========================================
# 2. 纯零样本预测逻辑 (DeepSeek Zero-shot)
# ==========================================
def zero_shot_predict(title):
    """
    完全不参考训练集，只给一个标题让 DeepSeek 硬猜。
    """
    # 稍微优化了 Prompt，让 DeepSeek 输出更稳定
    prompt = f"Please classify the following news title into one of these categories: {CATEGORIES}.\n\nTitle: {title}\n\nCategory (one word only):"

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that classifies news titles."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,  # 保持确定性
            max_tokens=15     # 限制输出长度
        )
        content = response.choices[0].message.content.strip().lower().replace(".", "")
        
        # 结果清洗与匹配
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
    # 1. 加载测试集
    try:
        print(f"🚀 正在加载测试数据: {TEST_PATH}")
        test_df = pd.read_excel(TEST_PATH)
    except Exception as e:
        print(f"❌ 读取文件失败: {e}")
        return

    results = []
    correct_count = 0
    
    print(f"📊 开始‘DeepSeek 零样本’推理（共 {len(test_df)} 条）...")
    
    for i in tqdm(range(len(test_df))):
        row = test_df.iloc[i]
        # 确保标签为字符串且小写
        true_label = str(row['section']).strip().lower()
        
        # 调用 DeepSeek 进行分类
        pred, raw_out = zero_shot_predict(row['title'])
        
        # 统计对错
        is_correct = 1 if pred == true_label else 0
        if is_correct: 
            correct_count += 1
        
        # 记录数据
        res_data = row.to_dict()
        res_data['编号'] = i + 1
        res_data['预测结果'] = pred
        res_data['是否正确'] = is_correct
        res_data['API原始输出'] = raw_out
        results.append(res_data)
        
        # 适当频率限制保护（DeepSeek 速度较快，0.01s 足够）
        time.sleep(0.01)

    # 2. 生成结果报表
    final_df = pd.DataFrame(results)
    accuracy = correct_count / len(test_df)
    
    print(f"\n🎯 DeepSeek Zero-shot 准确率: {accuracy:.2%}")
    
    output_name = "DeepSeek_Zero_Shot_Results.xlsx"
    final_df.to_excel(output_name, index=False)
    print(f"✅ 结果已保存至: {output_name}")

if __name__ == "__main__":
    main()