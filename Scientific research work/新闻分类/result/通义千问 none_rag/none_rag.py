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

TEST_PATH = r"C:\Users\Lenovo\Desktop\code\python\test1.xlsx"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
CATEGORIES = ["politics", "environment", "education", "world", "business", "technology", "science"]

# ==========================================
# 2. 纯零样本预测逻辑（保持不变，仅多要一句原因）
# ==========================================
def zero_shot_predict(title):
    prompt = (
        f"Classify this news title into one of: {CATEGORIES}.\n"
        f"Title: {title}\n"
        f"Return the category first, then briefly explain why."
    )

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=60
        )

        content = response.choices[0].message.content.strip().lower()

        pred_cat = "unknown"
        for c in CATEGORIES:
            if c in content:
                pred_cat = c
                break

        return pred_cat, content

    except Exception as e:
        return "error", str(e)

# ==========================================
# 3. 主程序（只改结果整理 & 输出）
# ==========================================
def main():
    print(f"🚀 正在加载测试数据: {TEST_PATH}")
    test_df = pd.read_excel(TEST_PATH)

    results = []
    correct_count = 0

    print(f"📊 开始 Zero-shot 推理（共 {len(test_df)} 条）...")

    for i in tqdm(range(len(test_df))):
        row = test_df.iloc[i]
        true_label = str(row['section']).strip().lower()

        pred, reason = zero_shot_predict(row['title'])

        is_correct = 1 if pred == true_label else 0
        if is_correct:
            correct_count += 1

        # ===== 核心：只改“文档输出结构” =====
        res_data = {
            "编号": i + 1,
            "title": row["title"],
            "section": row["section"],
            "预测结果": pred,
            "预测原因": reason,
            "是否正确": is_correct
        }

        # 如果原表还有其他列，一并追加
        for col in row.index:
            if col not in res_data:
                res_data[col] = row[col]

        results.append(res_data)
        time.sleep(0.01)

    final_df = pd.DataFrame(results)
    accuracy = correct_count / len(test_df)

    print(f"\n🎯 Zero-shot 实际准确率: {accuracy:.2%}")

    output_name = "Zero_Shot_55_Accuracy_Results.xlsx"
    final_df.to_excel(output_name, index=False)

    print(f"✅ 结果已保存至: {output_name}")

if __name__ == "__main__":
    main()
