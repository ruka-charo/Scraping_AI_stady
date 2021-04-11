import sqlite3


#%% sqliteのデータベースに接続
dbpath = 'test.sqlite'
conn = sqlite3.connect(dbpath)

# テーブルを作成し、データを挿入する
cur = conn.cursor()
cur.executescript('''
    /*itemsテーブルが既にあれば削除する*/
    DROP TABLE IF EXISTS items;

    /*テーブルの作成*/
    CREATE TABLE items(
        item_id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        price INTEGER
    );

    /*データを挿入*/
    INSERT INTO items(name, price)VALUES('Apple', 800);
    INSERT INTO items(name, price)VALUES('Orange', 780);
    INSERT INTO items(name, price)VALUES('Banana', 430);
''')

# 上記の操作をデータベースに反映させる
conn.commit()

# データを抽出する
cur = conn.cursor()
cur.execute('SELECT item_id, name, price FROM items')
item_list = cur.fetchall()

# 一行ずつ表示
for it in item_list:
    print(it)


#%% データベースに接続
filepath = 'test2.sqlite'
conn = sqlite3.connect(filepath)

# デーブルを作成
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS items')
cur.execute('''CREATE TABLE items(
    item_id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER
)''')
conn.commit()

# 単発でデータを挿入
cur = conn.cursor()
cur.execute(
    'INSERT INTO items (name, price) VALUES (?, ?)',
    ('Orange,', 520)
)
conn.commit()

# 連続でデータを挿入
cur = conn.cursor()
data = [("Mango",770), ("Kiwi",400), ("Grape",800),
    ("Peach",940),("Persimmon",700),("Banana", 400)]
cur.executemany(
    'INSERT INTO items (name, price) VALUES (?, ?)',
    data
)
conn.commit()

# 400〜700円のデータを抽出して表示
cur = conn.cursor()
price_range = (400, 700)
cur.execute(
    'SELECT * FROM items WHERE price>=? AND price<=?',
    price_range
)
fr_list = cur.fetchall()
for fr in fr_list:
    print(fr)
