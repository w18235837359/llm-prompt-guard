from guard.rule_guard import y_pred,y_true
from sklearn.metrics import (accuracy_score, # 准确率
                             f1_score, # F1分数
                             recall_score, # 召回率
                             precision_score, # 精确率
                             confusion_matrix # 混淆矩阵
                             )
accuracy = accuracy_score(y_true, y_pred)
# zero_division处理分母为零的结果 为0返回0
precision = precision_score(y_true, y_pred, zero_division=0)

recall = recall_score(y_true, y_pred, zero_division=0)

f1 = f1_score(y_true, y_pred, zero_division=0)

TN, FP, FN, TP = confusion_matrix(
    y_true, y_pred, labels=[0, 1]
# 展平成一维数组
).ravel()
def safe_div(a, b):
    return a / b if b != 0 else 0.0


fpr = safe_div(FP, FP + TN)
fnr = safe_div(FN, FN + TP)

print(f'准确率：{accuracy:.2%}')
print(f'精确率：{precision:.2%}')
print(f'召回率：{recall:.2%}')
print(f'F1分数：{f1:.2%}')
print(f'误报率：{fpr:.2%}')
print(f'漏报率：{fnr:.2%}')