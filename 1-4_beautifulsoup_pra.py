from urllib.parse import urljoin


'''相対パス → 絶対パス'''
base = 'http://example.com/html/a.html'

print(urljoin(base, 'b.html'))
print(urljoin(base, 'sub/c.html'))
print(urljoin(base, '../index.html'))
print(urljoin(base, '../img/hoge.png'))
print(urljoin(base, '../css/hoge.css'))
print(urljoin(base, '/hoge.html'))
print(urljoin(base, 'http://kujirahand.com/wiki'))
print(urljoin(base, '//uta.pw/shodou'))


#%%
'''まるごとダウンロード'''
from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import *
from os import makedirs
import os.path, time, re


#処理済みの判断変数
proc_files = {}

#HTML内にあるリンクを抽出する関数
def enum_links(html, base):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select("link[rel='stylesheet']")
    links += soup.select('a[href]')
    result = []
    #href属性を取り出し、リンクを絶対パスに変換
    for link in links:
        href = link.attrs['href']
        url = urljoin(base, href)
        result.append(url)
    return result

#ファイルをダウンロードし保存する関数
def download_file(url):
    o = urlparse(url)
    savepath = './' +o.netloc + o.path
    if re.search(r'/$', savepath):
        savepath += 'index.html'
    savedir = os.path.dirname(savepath)
    #すでにダウンロード済み？
    if os.path.exists(savepath):
        return savepath
    #ダウンロード先のディレクトリを作成
    if not os.path.exists(savedir):
        print('mkdir=', savedir)
        makedirs(savedir)
    #ファイルをダウンロード
    try:
        print('download=', url)
        urlretrieve(url, savepath)
        time.sleep(1)
        return savepath
    except:
        print('ダウンロード失敗：', url)
        return None

#HTMLを解析してダウンロードする関数
def analize_html(url, root_url):
    savepath = download_file(url)
    if savepath is None:
        return
    if savepath in proc_files:
        return
    proc_files[savepath] = True
    print('analize_html=', url)
    #リンクを抽出
    html = open(savepath, 'r', encoding='utf-8').read()
    links = enum_links(html, url)
    for link_url in links:
        #リンクがルート以外のパスを指していたら無視
        if link_url.find(root_url) != 0:
            if not re.search(r'.css$', link_url):
                continue
        #HTMLか？
        if re.search(r'.(html|htm)$', link_url):
            #再起的にHTMLファイルを解析
            analize_html(link_url, root_url)
            continue
        #それ以外のファイル
        download_file(link_url)

if __name__ == '__main__':
    #urlを丸ごとダウンロード
    url = 'https://docs.python.org/ja/3.6/library/'
    analize_html(url, url)
