%cd /Users/rukaoide/Library/Mobile Documents/com~apple~CloudDocs/Documents/Python/10_Scraping_AI_stady/6_Morphologic/data
from janome.tokenizer import Tokenizer
from gensim.models import word2vec
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Hiragino Sans'
plt.style.use('seaborn')
import re


#%% テキストファイルの読み込み
bindata = open('kokoro.txt', 'rb').read()
text = bindata.decode('shift_jis')

# テキストの先頭にあるヘッダとフッタを削除
text = re.split(r'\-{5,}',text)[2]
text = re.split(r'底本：', text)[0]
text = text.strip()

#%% 形態素解析
t = Tokenizer()
results = []

# テキストを一行ずつ処理
lines = text.split('\r\n')
for line in lines:
    s = line
    s = s.replace('|', '')
    s = re.sub(r'《.+?》', '', s) # ルビを削除
    s = re.sub(r'［＃.+?］', '', s) # 入力注を削除
    tokens = t.tokenize(s) # 形態素解析

    # 必要な語句だけを対象とする
    r = []
    for tok in tokens:
        if tok.base_form == '*': # 単語の基本形を採用
            w = tok.surface
        else:
            w = tok.base_form
        ps = tok.part_of_speech # 品詞情報
        hinsi = ps.split(',')[0]
        if hinsi in ['名詞', '形容詞', '動詞', '記号']:
            r.append(w)
    rl = (' '.join(r)).strip()
    results.append(rl)

#%% 書き込み先のテキストを開く
wakati_file = 'kokoro_wakati.txt'
with open(wakati_file, 'w', encoding='utf-8') as fp:
    fp.write('\n'.join(results))

#%% word2vecでモデルを作成
data = word2vec.LineSentence(wakati_file)
model = word2vec.Word2Vec(data, size=200, window=10, hs=1, min_count=2, sg=1)
model.save('kokoro.model')
print('ok')


'''モデルで遊ぶ'''
#%% モデル読み込み
model = word2vec.Word2Vec.load('kokoro.model')
#%% 「海」に近い単語
sim_word = model.most_similar(positive=['海'])

per = 1
for word in sim_word:
    plt.bar(word[0], word[1], color='green')
    plt.xlabel('類義語')
    plt.ylabel('度合い')
    if per > word[1]:
        per = word[1]
plt.ylim(word[1], 1)
plt.show()
