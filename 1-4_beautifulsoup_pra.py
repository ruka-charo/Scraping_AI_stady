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
