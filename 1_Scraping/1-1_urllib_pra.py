#ライブラリの読み込み
import sys
import urllib.request
import urllib.parse


'''urlretrieve()による保存'''

#%%URLと保存パスを指定
url = 'https://uta.pw/shodou/img/28/214.png'
savename = 'test.png'

#ダウンロード
urllib.request.urlretrieve(url, savename)
print('保存しました。')


'''urlopen()による保存'''

#%%URLと保存パスを指定
url = 'https://uta.pw/shodou/img/28/214.png'
savename = 'test_2.png'

#ダウンロード
mem = urllib.request.urlopen(url).read()

#ファイルへ保存
with open(savename, mode='wb') as f:
    f.write(mem)
    print('保存しました。')


'''Webからデータを取得'''

#%%データの取得
url = 'https://api.aoikujira.com/ip/ini'
res = urllib.request.urlopen(url)
data = res.read()

#バイナリーを文字列に変換
text = data.decode('utf-8')
print(text)


'''任意のパラメータをつけてリクエストを送信'''

#%%
API = 'https://api.aoikujira.com/zip/xml/get.php'

#パラメータをURLエンコードする。
values = {
    'fmt': 'xml',
    'zn': '1200037'
}
params = urllib.parse.urlencode(values)

#リクエスト用のURLを生成
url = API + '?' + params
print('url=', url)

#ダウンロード
data = urllib.request.urlopen(url).read()
text = data.decode('utf-8')
print(text)
