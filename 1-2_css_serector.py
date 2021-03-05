from bs4 import BeautifulSoup
import urllib.request as req
import re


'''CSSセレクタの練習1'''
#%%
url = 'https://www.aozora.gr.jp/index_pages/person148.html'
res = req.urlopen(url)

#HTMLの解析
soup = BeautifulSoup(res, 'html.parser')

#データ抽出
lists = soup.select('body > ol:nth-child(8) > li > a')

for name in lists:
    href = name.attrs['href']
    title = name.string
    print(title, '\n', href)


'''CSSセレクタの練習2'''
#%%
html = '''
<ul id="bible">
  <li id="ge">Genesis</li>
  <li id="ex">Exodus</li>
  <li id="le">Leviticus</li>
  <li id="nu">Numbers</li>
  <li id="de">Deuteronomy</li>
</ul>
'''
soup = BeautifulSoup(html, 'html.parser')

#cssセレクタで検索する方法
sel = lambda q: print(soup.select_one(q).string)
sel('#nu')
sel('li#nu')
sel('ul > li#nu')
sel('#bible #nu')
sel('#bible > #nu')
sel('ul#bible > li#nu')
sel("li[id='nu']")
sel('li:nth-of-type(4)')

#その他の方法
print(soup.select('li')[3].string)
print(soup.find_all('li')[3].string)


'''複雑なCSSセレクタの練習'''
#%%
html = '''
<html><body>
<div id="main-goods" role="page">
  <h1>フルーツや野菜</h1>
  <ul id="fr-list">
    <li class="red green" data-lo="jp">リンゴ</li>
    <li class="purple" data-lo="us">ブドウ</li>
    <li class="yellow" data-lo="us">レモン</li>
    <li class="yellow" data-lo="jp">オレンジ</li>
  </ul>
  <ul id="ve-list">
    <li class="white green" data-lo="jp">ダイコン</li>
    <li class="red green" data-lo="us">パプリカ</li>
    <li class="black" data-lo="jp">ナス</li>
    <li class="black" data-lo="us">アボカド</li>
    <li class="white" data-lo="cn">レンコン</li>
  </ul>
</div>
<body></html>
'''

soup = BeautifulSoup(html, 'html.parser')

#CSSセレクタで呼び出す。
print(soup.select('li')[7].string)
print(soup.select_one('#ve-list > li:nth-of-type(4)').string)
print(soup.select("#ve-list > li[data-lo='us']")[1].string)
print(soup.select('#ve-list > li.black')[1].string)

#findメソッドで選び出す。
cond = {'data-lo': 'us', 'class': 'black'}
print(soup.find('li', cond).string)

#findメソッドを２回組み合わせる。
print(soup.find(id='ve-list').find('li', cond).string)


'''正規表現との組み合わせ'''
#%%
html = """
<ul>
  <li><a href="hoge.html">hoge</li>
  <li><a href="https://example.com/fuga">fuga*</li>
  <li><a href="https://example.com/foo">foo*</li>
  <li><a href="http://example.com/aaa">aaa</li>
</ul>
"""

soup = BeautifulSoup(html, 'html.parser')

#正規表現でhrefからhttpsのものを抽出。
li = soup.find_all(href=re.compile(r'^https://'))
for e in li:
    print(e.attrs['href'])
