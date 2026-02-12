import pandas as pd
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import os

# 1. 定义文件名字列表 (按照你的要求顺序)
file_names = [
    "通义千问+cot+none_rag", "通义千问+cot+rag1", "通义千问+cot+rag2",
    "通义千问+none_cot+none_rag", "通义千问+none_cot+rag1", "通义千问+none_cot+rag2",
    "deepseek+cot+none_rag", "deepseek+cot+rag1", "deepseek+cot+rag2",
    "deepseek+none_cot+none_rag", "deepseek+none_cot+rag1", "deepseek+none_cot+rag2"
]

# 2. 定义文件地址列表 (请注意检查第6个地址，你提供的信息中它与第5个重复了)
# 使用 raw string (r"...") 以避免Windows路径中的反斜杠转义问题
file_paths = [
    r"C:\Users\Lenovo\Desktop\code\python\result\通义千问API\通义千问 none_cot none_rag 59.05.xlsx",
    r"C:\Users\Lenovo\Desktop\code\python\result\通义千问API\通义千问 none_cot rag1 77.62%.xlsx",
    r"C:\Users\Lenovo\Desktop\code\python\result\通义千问API\通义千问 none_cot rag2 74.76%.xlsx",
    r"C:\Users\Lenovo\Desktop\code\python\result\通义千问 cot\通义千问 cot none_rag 67.14%.xlsx",
    r"C:\Users\Lenovo\Desktop\code\python\result\通义千问 cot\通义千问 cot rag1 78.57%.xlsx",
    r"C:\Users\Lenovo\Desktop\code\python\result\通义千问 cot\通义千问 cot rag2 76.67%.xlsx", # 注意：这里你原本给的是重复的rag1地址，如果是rag2请修改此处
    r"C:\Users\Lenovo\Desktop\code\python\result\deepseek API\deepseek none_cot none_rag 50.95%.xlsx",
    r"C:\Users\Lenovo\Desktop\code\python\result\deepseek API\deepseek none_cot rag1 83.81%.xlsx",
    r"C:\Users\Lenovo\Desktop\code\python\result\deepseek API\deepseek none_cot rag2 78.10%.xlsx",
    r"C:\Users\Lenovo\Desktop\code\python\result\deepseek cot\deepseek cot none_rag 69.52%.xlsx",
    r"C:\Users\Lenovo\Desktop\code\python\result\deepseek cot\deepseek cot rag1 79.05%.xlsx",
    r"C:\Users\Lenovo\Desktop\code\python\result\deepseek cot\deepseek cot rag2 82.86%.xlsx"
]

# 3. 定义数据清洗函数 (针对Deepseek可能出现的“标签+解释”的情况)
def clean_label(text):
    if pd.isna(text):
        return ""
    text = str(text).lower().strip()
    # 如果预测结果包含换行符（例如Deepseek解释了原因），只取第一行
    if '\n' in text:
        text = text.split('\n')[0].strip()
    # 移除可能存在的标点，如句号
    text = text.replace('.', '').replace('category:', '').strip()
    return text

# 4. 循环计算指标
results = []

for name, path in zip(file_names, file_paths):
    try:
        # 读取Excel文件
        df = pd.read_excel(path)
        
        # 确保关键列存在 (根据你的截图，真实标签是 'section'，预测标签是 '预测结果')
        # 如果列名有细微差别（比如空格），这里会报错，需要根据实际情况微调
        true_col = 'section'
        pred_col = '预测结果'
        
        if true_col not in df.columns or pred_col not in df.columns:
            print(f"Error in {name}: Columns not found.")
            results.append({'文件名': name, '准确率': 0, '精确率': 0, '召回率': 0, 'F1': 0})
            continue

        # 数据清洗：转为小写，去除多余空格和解释性文字
        y_true = df[true_col].apply(clean_label)
        y_pred = df[pred_col].apply(clean_label)
        
        # 计算指标
        # average='weighted' 适用于多分类任务，考虑了样本不平衡
        acc = accuracy_score(y_true, y_pred)
        prec, rec, f1, _ = precision_recall_fscore_support(y_true, y_pred, average='weighted', zero_division=0)
        
        # 存入列表，保留4位小数
        results.append({
            '文件名': name,
            '准确率': round(acc, 4),
            '精确率': round(prec, 4),
            '召回率': round(rec, 4),
            'F1': round(f1, 4)
        })
        
    except Exception as e:
        print(f"处理文件 {name} 时出错: {e}")
        results.append({'文件名': name, '准确率': 'Error', '精确率': 'Error', '召回率': 'Error', 'F1': 'Error'})

# 5. 生成最终表格
result_df = pd.DataFrame(results)

# 按照你要求的格式调整：第一列是文件名，后面是指标
# 设置索引为文件名，以便转置或直接显示
result_df.set_index('文件名', inplace=True)

print("-" * 30)
print("计算完成，结果如下：")
print("-" * 30)
print(result_df)

# 6. (可选) 保存为Excel文件
output_path = r"C:\Users\Lenovo\Desktop\code\python\result\evaluation_summary.xlsx"
result_df.to_excel(output_path)
print(f"\n结果已保存至: {output_path}")