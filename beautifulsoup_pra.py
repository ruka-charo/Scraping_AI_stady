#ライブラリを読み込む
from bs4 import BeautifulSoup
import urllib.request as req


'''基本的な使い方'''

#%%解析したいHTML
html = '''
<html><body>
    <h1>スクレイピングとは？</h1>
    <p>Webページを解析すること。</p>
    <p>任意の箇所を抽出すること。</p>
</body></html>
'''

#HTMLを解析する。
soup = BeautifulSoup(html, 'html.parser')

#任意の部分を抽出する。
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

#要素のテキストを表示する。
print('h1 = ' + h1.string)
print('p  = ' + p1.string)
print('p  = ' + p2.string)


'''任意のidで探す方法'''
#%%
html = '''
<html><body>
    <h1 id='title'>スクレイピングとは？</h1>
    <p id='body'>Webページから任意のデータを抽出すること。</p>
</body></html>
'''

#HTMLを解析する。
soup = BeautifulSoup(html, 'html.parser')

#find()メソッドで取り出す。
title = soup.find(id='title')
body = soup.find(id='body')

#テキスト部分を表示
print('#title=' + title.string)
print('#body=' + body.string)


'''複数の要素を取得する'''
#%%
html = """
<html><body>
  <ul>
    <li><a href="http://uta.pw">uta</a></li>
    <li><a href="http://oto.chu.jp">oto</a></li>
  </ul>
</body></html>
"""

#HTMLを解析する。
soup = BeautifulSoup(html, 'html.parser')

#find_all()メソッドで取り出す。
links = soup.find_all('a')

#リンク一覧を表示
for a in links:
    href = a.attrs['href']
    text = a.string
    print(text, '>', href)


'''urlopen()との組み合わせ'''

#%%
url = 'https://api.aoikujira.com/zip/xml/1200037'

#urlopen()でデータを取得する。
res = req.urlopen(url)

#BeautifulSoupで解析
soup = BeautifulSoup(res, 'html.parser')

#任意のデータを抽出
ken = soup.find('ken').string
shi = soup.find('shi').string
cho = soup.find('cho').string
print(ken, shi, cho)


'''CSSセレクタを使う'''

#%%解析対象となるHTML
html = """
<html><body>
<div id="meigen">
  <h1>トルストイの名言</h1>
  <ul class="items">
    <li>汝の心に教えよ、心に学ぶな</li>
    <li>謙虚な人は誰からも好かれる。</li>
    <li>強い人々は、いつも気取らない。</li>
  </ul>
</div>
</body></html>
"""

#HTMLを解析する。
soup = BeautifulSoup(html, 'html.parser')

#必要な部分をCSSクエリで取り出す。
#タイトル部分を取得
h1 = soup.select_one('div#meigen > h1').string
print('h1 =', h1)

#リスト部分を取得
li_list = soup.select('div#meigen > ul.items > li')
for li in li_list:
    print('li =', li.string)
