import pandas as pd


# Excelファイルを開く
filename = 'population.xlsx'
sheet_name = 'list-sjis.csv'
book = pd.read_excel(filename, sheet_name=sheet_name)

# データを人口順に表示
book.sort_values(by='法定人口', ascending=False)
print(book)
