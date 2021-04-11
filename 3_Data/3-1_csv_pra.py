import codecs, csv


#%% Shift_JISのCSVファイルを読む
filename = 'list-sjis.csv'
csv = codecs.open(filename, 'r', 'shift_jis').read()

# CSVをPythonのリストに変換する
data = []
rows = csv.split('\r\n')
for row in rows:
    if row == '':
        continue
    cells = row.split(',')
    data.append(cells)

# 変換結果を表示
for c in data:
    print(c[1], c[2])


#%% CSVファイルを開く
filename = 'list-sjis.csv'
fp = codecs.open(filename, 'r', 'shift_jis')

#1行ずつ読む
reader = csv.reader(fp, delimiter=',', quotechar='"')
for cells in reader:
    print(cells[1], cells[2])

#%% CSVファイルに書き込む
with codecs.open('test.csv', 'w', 'shift_jis') as fp:
    writer = csv.writer(fp, delimiter=',', quotechar='"')
    writer.writerow(['ID', '商品名', '値段'])
    writer.writerow(['1000', 'SDカード', 300])
    writer.writerow(["1001", "キーボード", 2100])
    writer.writerow(["1002", "マジック(赤,青)", 150])
