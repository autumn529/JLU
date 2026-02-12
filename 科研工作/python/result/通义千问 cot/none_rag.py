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

CATEGORIES = ["politics", "environment", "education", "world",
              "business", "technology", "science"]

# ==========================================
# 2. Zero-shot + 隐式 CoT（关键修改点）
# ==========================================
def zero_shot_predict(title):
    prompt = f"""
You are a professional news classifier.

Before answering, carefully reason step by step internally.
Do NOT reveal your reasoning.

Categories: {CATEGORIES}

Title: {title}

Output format:
Category: <one category>
Reason: <short explanation>
"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=120
        )

        content = response.choices[0].message.content.strip()

        pred, reason = "unknown", content
        for line in content.split("\n"):
            if line.lower().startswith("category:"):
                v = line.split(":", 1)[1].strip().lower()
                if v in CATEGORIES:
                    pred = v
            elif line.lower().startswith("reason:"):
                reason = line.split(":", 1)[1].strip()

        return pred, reason

    except Exception as e:
        return "error", str(e)

# ==========================================
# 3. 主程序（文档输出不变）
# ==========================================
def main():
    test_df = pd.read_excel(TEST_PATH)

    results = []
    correct = 0

    for i in tqdm(range(len(test_df))):
        row = test_df.iloc[i]
        true_label = row["section"].strip().lower()

        pred, reason = zero_shot_predict(row["title"])
        ok = int(pred == true_label)
        correct += ok

        res = row.to_dict()
        res["编号"] = i + 1
        res["预测结果"] = pred
        res["预测原因"] = reason
        res["是否正确"] = ok
        results.append(res)

        time.sleep(0.01)

    final_df = pd.DataFrame(results)

    cols = final_df.columns.tolist()
    cols.remove("编号")
    final_df = final_df[["编号"] + cols]

    cols = final_df.columns.tolist()
    idx = cols.index("section") + 1
    insert = ["预测结果", "预测原因", "是否正确"]
    rest = [c for c in cols if c not in insert]
    final_df = final_df[rest[:idx] + insert + rest[idx:]]

    print(f"🎯 Zero-shot 隐式 CoT 准确率: {correct / len(test_df):.2%}")
    final_df.to_excel("ZeroShot_ImplicitCoT.xlsx", index=False)

if __name__ == "__main__":
    main()
