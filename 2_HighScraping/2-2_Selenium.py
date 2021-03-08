from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''ヘッドレスでスクリーンショットを撮る'''
#%%
url = "https://www.aozora.gr.jp/cards/000081/files/46268_23911.html"

#GoogleChromeのヘッドレスモードを有効にする。
options = Options()
options.add_argument('-headless')

#GoogleChromeを起動する。
browser = webdriver.Chrome(options=options)

#URLを読み込む
browser.get(url)

#画面をキャプチャーしてファイルに保存
browser.save_screenshot('website.png')

#ブラウザの終了
browser.quit()


'''会員制Webサイトにログインする'''
#%%
USER = "JS-TESTER"
PASS = "ipCU12ySxI"

#Chromeのドライバーを得る。
options = Options()
options.add_argument('-headless')
browser = webdriver.Chrome(options=options)

#ログインページにアクセス
url_login = 'https://uta.pw/sakusibbs/users.php?action=login'
browser.get(url_login)
print('ログインページにアクセスしました。')

#テキストボックスに文字を入力
e = browser.find_element_by_id('user')
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id('pass')
e.clear()
e.send_keys(PASS)

#フォームを送信
form = browser.find_element_by_css_selector('#loginForm > form')
form.submit()
print('情報を入力してログインボタンを押しました。')

#ページのロード完了まで待機
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#header_menu > span'))
)

#マイページのURLを得る。
a = browser.find_element_by_css_selector('#header_menu > span > a')
url_mypage = a.get_attribute('href')
print('マイページのURL=', url_mypage)

#マイページを表示
browser.get(url_mypage)

#お気に入りのタイトルを列挙
links = browser.find_elements_by_css_selector(
    '#favlist > li > a'
)
for a in links:
    href = a.get_attribute('href')
    title = a.text
    print('-', title, '>', href)


'''JavaScriptを実行してみよう'''
#%%Chromeのドライバーを得る。
options = Options()
options.add_argument('-headless')
browser = webdriver.Chrome(options=options)

#適当なWebサイトを開く
browser.get('https://google.com')

#JavaScriptを実行
r = browser.execute_script('return 100 + 50')
print(r)
