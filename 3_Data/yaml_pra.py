import yaml


#%% YAMLの定義 ---- (※1)
yaml_str = """
Date: 2017-03-10
PriceList:
    -
        item_id: 1000
        name: Banana
        color: yellow
        price: 800
    -
        item_id: 1001
        name: Orange
        color: orange
        price: 1400
    -
        item_id: 1002
        name: Apple
        color: red
        price: 2400
"""

# YAMLを解析する
data = yaml.load(yaml_str)

# 名前と値段だけ表示する
for item in data['PriceList']:
    print(item['name'], item['price'])


#%% Pythonのデータをyamlで出力
customer = [
    { "name": "Yamada", "age": "35", "gender": "man"  },
    { "name": "Sato",   "age": "58", "gender": "woman" },
    { "name": "Kato",   "age": "42", "gender": "man" },
    { "name": "Nishi",  "age": "22", "gender": "man" }
]

# Pythonのデータをyamlに変換
yaml_str = yaml.dump(customer)
print(yaml_str)
print('--- --- ---')

# yamlをPythonデータに変換
data = yaml.load(yaml_str)

# 顧客名だけを表示
for p in data:
    print(p['name'])
