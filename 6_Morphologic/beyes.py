%cd /Users/rukaoide/Library/Mobile Documents/com~apple~CloudDocs/Documents/Python/10_Scraping_AI_stady/6_Morphologic/data
from janome.tokenizer import Tokenizer
from math

#%% ベイジアンフィルター
class BayesianFilter:
    def __init__(self):
        self.words = set() # 出現した単語を全て記録
        self.word_dict = {} # カテゴリごとの単語出現回数を記録
        self.category_dict = {} # カテゴリの出現回数を記録

    # 形態素解析を行う
    def split(self, text):
        result = []
        t = Tokenizer()
        malist = t.tokenizer(text)
        for w in malist:
            sf = w.surface # 区切られた単語そのまま
            bf = w.base_form # 単語の基本形
            if bf == '' or bf == '*':
                bf = sf
            result.append(bf)
        return result

    # 単語とカテゴリを数える処理
    def inc_word(self, word, category):
        # 単語をカテゴリに追加
        if not category in self.word_dict:
            self.word_dict[category] = {}
        if not word in self.word_dict[category]:
            self.word_dict[category][word] = 0
        self.word_dict[category][word] += 1
        self.words.add(word)
    def inc_category(self, category):
        # カテゴリを加算する
        if not category in self.category_dict:
            self.category_dict[category] = 0
        self.category_dict[category] += 1

    # テキストを学習する
    def fit(self, text, category):
        word_list = self.split(text)
        for word in word_list:
            self.inc_word(word, category)
        self.inc_category(category)

    # カテゴリにおける単語リストのスコアを計算する
    def score(self, words, category):
        score = math.log(self.category_prob(category))
        for word in words:
            score += math.log(self.word_prob(word, category))
        return score

    # テキストのカテゴリ分けを行う
