import pandas as pd
import time
import re
from tqdm import tqdm
from openai import OpenAI

# ==========================================
# 1. 核心配置
# ==========================================
# 你的 DeepSeek API Key
API_KEY = "sk-aadf9b32e16d47ecbc4eeff3166c23fb"
# DeepSeek 标准 API 地址
BASE_URL = "https://api.deepseek.com"
# 使用 DeepSeek V3 模型
MODEL_NAME = "deepseek-chat"

# 测试集路径
TEST_PATH = r"C:\Users\Lenovo\Desktop\code\python\test1.xlsx"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
CATEGORIES = ["politics", "environment", "education", "world", "business", "technology", "science"]

# ==========================================
# 2. 思维链预测逻辑 (Zero-shot CoT)
# ==========================================
def zero_shot_cot_predict(title):
    """
    不参考外部数据库，仅通过思维链引导 DeepSeek 进行逻辑推理。
    """
    # 构造思维链 Prompt
    prompt = f"""Task: Classify the following news title into one of these categories: {CATEGORIES}.

[Target News Title]
{title}

Instruction:
1. Analyze the core subject and specific keywords of the title.
2. Reason step-by-step about which category it fits best.
3. Compare with similar categories to ensure accuracy.
4. Output your reasoning and the final category.

Response Format:
Reasoning: [Brief English reasoning]
Category: [Exact category name from the list]
"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a professional news analyst. Think logically and concisely."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,  # 低温度确保推理逻辑的一致性
            max_tokens=200    # 足够模型写下推理过程
        )
        content = response.choices[0].message.content.strip()
        
        # --- 解析逻辑 ---
        # 1. 使用正则匹配 Category: 后的单词
        cat_match = re.search(r"Category:\s*(\w+)", content, re.IGNORECASE)
        pred_cat = cat_match.group(1).lower() if cat_match else "unknown"
        
        # 2. 兜底策略：如果模型没按格式出牌，在内容中查找关键词
        if pred_cat not in CATEGORIES:
            # 仅在推理结果的后半部分寻找，减少推理干扰
            search_area = content.lower().split('category:')[-1]
            for c in CATEGORIES:
                if c in search_area:
                    pred_cat = c
                    break
        
        return pred_cat, content
    except Exception as e:
        return "error", str(e)

# ==========================================
# 3. 执行主程序
# ==========================================
def main():
    # 1. 加载测试集
    try:
        print(f"🚀 正在读取测试文件: {TEST_PATH}")
        test_df = pd.read_excel(TEST_PATH)
    except Exception as e:
        print(f"❌ 文件读取失败: {e}")
        return

    results = []
    correct_count = 0
    
    print(f"📊 启动 DeepSeek Zero-shot CoT 推理（共 {len(test_df)} 条）...")
    
    # 2. 循环预测
    for i in tqdm(range(len(test_df))):
        row = test_df.iloc[i]
        true_label = str(row['section']).strip().lower()
        
        # 调用 CoT 预测
        pred, full_output = zero_shot_cot_predict(row['title'])
        
        # 判定对错
        is_correct = 1 if pred == true_label else 0
        if is_correct: 
            correct_count += 1
        
        # 收集结果
        res_data = row.to_dict()
        res_data['编号'] = i + 1
        res_data['预测结果'] = pred
        res_data['模型推理过程'] = full_output
        res_data['是否正确'] = is_correct
        results.append(res_data)
        
        # 避免请求过快，微小停顿
        time.sleep(0.01)

    # 3. 统计与保存
    final_df = pd.DataFrame(results)
    
    # 整理列顺序：将结果列放在 section 之后
    cols = list(test_df.columns)
    sec_idx = cols.index('section') + 1
    new_cols = ['编号'] + cols[:sec_idx] + ['预测结果', '模型推理过程', '是否正确'] + cols[sec_idx:]
    final_df = final_df[list(dict.fromkeys(new_cols))]

    accuracy = correct_count / len(test_df)
    print(f"\n🎯 DeepSeek CoT 最终准确率: {accuracy:.2%}")
    
    output_name = "DeepSeek_ZeroShot_CoT_Report.xlsx"
    final_df.to_excel(output_name, index=False)
    print(f"✅ 报表已生成至: {output_name}")

if __name__ == "__main__":
    main()