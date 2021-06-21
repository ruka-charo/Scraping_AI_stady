%cd /Users/rukaoide/Library/Mobile Documents/com~apple~CloudDocs/Documents/Python/10_Scraping_AI_stady/6_Morphologic/data
from janome.tokenizer import Tokenizer
import os, glob


# Janomeを用いて形態素解析を行う
ja_tokenizer = Tokenizer()

# 日本語の分かち書き
def ja_tokenize(text):
    res = []
    lines = text.split('\n')
    lines = lines[2:] # 最初の2行はヘッダー情報なので捨てる
    for line in lines:
        malist = ja_tokenizer.tokenize(line)
        for tok in malist:
            # 品詞だけ取り出す
            ps = tok.part_of_speech.split(',')[0]
            if not ps in ['名詞', '動詞', '形容詞']:
                continue
            # 単語の取り出し
            w = tok.base_form
            if w == '*' or w == '':
                w = tok.surface # 文章中のそのままの形
            if w == '' or w == '\n':
                continue
            res.append(w)
        res.append('\n')
    return res


# テストデータの読み込み
root_dir = './newstext'
# 指定ディレクトリ以下のテキストファイルを抽出
for path in glob.glob(root_dir+'/*/*.txt', recursive=True):
    if path.find('LICENSE') > 0:
        continue
    print(path)
    path_wakati = path + '.wakati'
    if os.path.exists(path_wakati):
        continue
    text = open(path, 'r').read()
    words = ja_tokenize(text)
    wt = ' '.join(words)
    open(path_wakati, 'w', encoding='utf-8').write(wt)
