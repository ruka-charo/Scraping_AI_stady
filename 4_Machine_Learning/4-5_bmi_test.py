from sklearn import svm, metrics
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


# データの読み込み
csv = pd.read_csv('bmi.csv')

# 解析対象のデータ
h = csv['height']
w = csv['weight']
csv_data = pd.concat([h, w], axis=1)
csv_label = csv['label']

# 学習用とテスト用に分割
train_data, test_data, train_label, test_label = train_test_split(
    csv_data, csv_label)

# 学習
clf = svm.SVC()
clf.fit(train_data, train_label)

# 予測
pre = clf.predict(test_data)

# 正解率
ac_score = metrics.accuracy_score(test_label, pre)
print('正解率：', ac_score)
cl_report = metrics.classification_report(test_label, pre)
print('レポート=')
print(cl_report)
