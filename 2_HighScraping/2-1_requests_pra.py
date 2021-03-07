import requests


#%%データを取得
r = requests.get('https://api.aoikujira.com/time/get.php')

#テキスト形式でデータを得る。
text = r.text
print(text)

#バイナリー形式でデータを得る。
bin = r.content
print(bin)


#%%画像データを取得
r = requests.get('https://uta.pw/shodou/img/3/3.png')

#バイナリー形式でデータを得て保存
with open('test.png', 'wb') as f:
    f.write(r.content)

print('saved')
