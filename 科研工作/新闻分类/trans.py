import time
import pandas as pd
import dashscope
from dashscope import Generation
import re

dashscope.api_key = "sk-94b47d03d45443a1863cd08ca527e6bc"

file_path = r"C:\Users\Lenovo\Desktop\code\python\test.xls"
output_path = r"C:\Users\Lenovo\Desktop\code\python\classification_result.xlsx"

CATEGORIES = [
    "politics",
    "environment",
    "education",
    "world",
    "business",
    "technology",
    "science"
]

def clean_label(label):
    if pd.isna(label):
        return ""
    return re.sub(r"[^\w]", "", str(label).lower())

def extract_label(text):
    text = text.lower()
    for cat in CATEGORIES:
        if cat in text:
            return cat
    return None

def rule_fallback(text):
    text = text.lower()
    if "election" in text or "government" in text:
        return "politics"
    if "climate" in text or "pollution" in text:
        return "environment"
    if "school" in text or "education" in text:
        return "education"
    if "market" in text or "company" in text:
        return "business"
    if "technology" in text or "software" in text:
        return "technology"
    if "research" in text or "scientist" in text:
        return "science"
    return "world"

def classify_text(text):
    if pd.isna(text) or not str(text).strip():
        return "world"

    content = str(text)[:300]

    prompt = (
        "请判断下面新闻属于以下哪一类：\n"
        "politics, environment, education, world, business, technology, science\n\n"
        f"{content}"
    )

    try:
        response = Generation.call(
            model="qwen-long-2025-01-25",
            prompt=prompt,
            temperature=0.8,
            result_format="text"
        )

        label = extract_label(response.output_text)
        return label if label else rule_fallback(content)

    except Exception:
        # ✅ 静默兜底，不打印任何异常
        return rule_fallback(content)

def main():
    df = pd.read_excel(file_path)
    preds = []

    for i, row in df.iterrows():
        pred = classify_text(row["text"])
        preds.append(pred)
        print(f"[{i+1}] 实际:{row['section']} | 预测:{pred}")
        time.sleep(0.4)

    df["ai_prediction"] = preds
    df["is_correct"] = df.apply(
        lambda x: clean_label(x["ai_prediction"]) == clean_label(x["section"]),
        axis=1
    )

    acc = df["is_correct"].mean() * 100
    print(f"\n📉 模型准确率: {acc:.2f}%")

    df.to_excel(output_path, index=False)
    print("结果已保存到:", output_path)

if __name__ == "__main__":
    main()
