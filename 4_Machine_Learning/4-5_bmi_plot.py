import matplotlib.pyplot as plt
import pandas as pd


# pandasでcsvファイルを読み込む
data = pd.read_csv('bmi.csv', index_col=2)

# 描画を開始する
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# サブプロット用 - 指定のラベルを任意の色で描画
def scatter(lbl, color):
    b = data.loc[lbl]
    ax.scatter(b['height'], b['weight'], c=color, label=lbl)

scatter('fat', 'red')
scatter('normal', 'yellow')
scatter('thin', 'blue')

ax.legend()
plt.show()
