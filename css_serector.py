from bs4 import BeautifulSoup
import urllib.request as req


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
