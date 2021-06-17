%cd /Users/rukaoide/Library/Mobile Documents/com~apple~CloudDocs/Documents/Python/10_Scraping_AI_stady/6_Morphologic/data
from janome.tokenizer import Tokenizer


#%% テキストファイルの読み込み
with open('gingatetsudono_yoru.txt', 'r', encoding='shift_jis') as file:
    txt = file.read()

#%% 形態素解析オブジェクトの生成
t = Tokenizer()

# テキストを一行ずつ処理
word_dic = {}
lines = txt.split('\r\n')

for line in lines:
    malist = t.tokenize(line)
    for w in malist:
        word = w.surface # 単語情報
        ps = w.part_of_speech # 品詞情報
        if ps.find('名詞') < 0:
            continue # 名詞だけカウント
        if not word in word_dic:
            word_dic[word] = 0
        word_dic[word] += 1 # カウント

#%% よく使われる単語を表示
keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
for word, cnt in keys[:50]:
    print('{0}({1})'.format(word, cnt))
