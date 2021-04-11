import openpyxl


# Excelファイルを開く
filename = 'population.xlsx'
book = openpyxl.load_workbook(filename)

# アクティブになっているシートを得る
sheet = book.active

# 人口のトータルを計算する
total = 0
for i, row in enumerate(sheet.rows):
    if i == 0:
        continue
    po = int(row[2].value)
    total += po
print('total=', total)

# 書き込む
sheet['A49'] = 'Total'
sheet['C49'] = total

# 書き込んだ内容をファイルに保存
filename = 'population-total.xlsx'
book.save(filename)
print('ok')
