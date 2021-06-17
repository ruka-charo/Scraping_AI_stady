import MeCab
from janome.tokenizer import Tokenizer


#%% MeCabでの形態素解析
mecab = MeCab.Tagger('-Ochasen')
malist = mecab.parse('私は犬が好きです。')
print(malist)

#%% Janomeでの形態素解析
t = Tokenizer()
malist = t.tokenize('私は犬が好きです。')
for i in malist:
    print(i)
