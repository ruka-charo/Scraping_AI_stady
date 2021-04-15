import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split


# データの読み込み
mr = pd.read_csv('mushroom.csv', header=None)

# データ内の記号を数値に変換する
label = []
data = []
attr_list = []

for row_index, row in mr.iterrows():
    label.append(row.loc[0])
    row_data = []
    for v in row.loc[1:]:
        row_data.append(ord(v))
    data.append(row_data)

# 学習用とテスト用データに分ける
train_data, test_data, train_label, test_label = train_test_split(
    data, label)

# データの学習
clf = RandomForestClassifier()
clf.fit(train_data, train_label)

# データの予測
pre = clf.predict(test_data)

# 正解率
ac_score = metrics.accuracy_score(test_label, pre)
cl_report = metrics.classification_report(test_label, pre)
print('正解率：', ac_score)
print('レポート=\n', cl_report)
