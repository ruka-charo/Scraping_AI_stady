%cd /Users/rukaoide/Library/Mobile Documents/com~apple~CloudDocs/Documents/Python/10_Scraping_AI_stady/6_Morphologic
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import json
import cloudpickle


# パラメータ
nb_classes = 9
batch_size = 64
nb_epoch = 20


#%% MLPモデルを生成
def build_model():
    global max_words
    model = Sequential()
    model.add(Dense(512, input_shape=(max_words,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(cb_classes))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy'])
    return model


#%% データの読み込み
data = json.load(open('./data/newstext/data-mini.json'))

X = np.array(data['X']) # テキストを表すデータ
Y = np.array(data['Y']) # カテゴリデータ
# 最大単語数を指定
max_words = len(X[0])

# 学習
X_train, X_test, y_train, y_test = train_test_split(X, Y)
print(len(X_train), len(y_train))
y_train = np_utils.to_categorical(y_train, nb_classes)
model = KerasClassifier(build_fn=build_model,
                        epochs = nb_epoch,
                        batch_size = batch_size)
model.fit(X_train, y_train)

#%% 予測
y = model.predict(X_test)
ac_score = metrics.accuracy_score(y_test, y)
cl_report = metrics.classification_report(y_test, y)
print('正解率:', ac_score)
print('レポート:', cl_report)
