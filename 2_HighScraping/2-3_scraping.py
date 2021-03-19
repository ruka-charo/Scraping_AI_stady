from bs4 import BeautifulSoup
from urllib.parse import *
from urllib.request import *
import os, os.path, time

#%%
# リンクの抽出
html = open('eki-link.html', encoding='utf-8').read()
soup = BeautifulSoup(html, 'html.parser')
links = soup.select('a[href]')

result = []
for a in links:
    href = a.attrs['href']
    title = a.string
    result.append((title, href))

# リンク先をダウンロードする。
savepath = './out';
if not os.path.exists(savepath): os.mkdir(savepath)
for title, url in result:
    path = savepath + '/' + url + '.html'
    # 相対URLを絶対URLに変換
    a_url = urljoin('http://example.com', url)
    print('download=' + a_url)
    # ここでダウンロードを行う。
    urlretrieve(a_url, path)
    time.sleep(1)

#%%
# csvファイルに保存
html = open('eki-link.html', encoding='utf-8').read()
soup = BeautifulSoup(html, 'html.parser')

# テーブルを解析する。
result = []

# <table>タグを得る。
table = soup.select_one('table')

# <tr>タグを得る。
tr_list = table.find_all('tr')
for tr in tr_list:
    # <td>あるいは<th>タグを得る。
    result_row = []
    td_list = tr.find_all(['td', 'th'])
    for td in td_list:
        cell = td.get_text()
        result_row.append(cell)
    result.append(result_row)

# リストをcsvファイルとして出力
for row in result:
    print(','.join(row))
