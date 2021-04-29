from selenium import webdriver
import datetime
import random
import time

wd  = webdriver.Chrome()
wd.get('https://www.instagram.com')
time.sleep(1)

#ログインする
def login():
    wd.find_element_by_name('username').send_keys(username)
    time.sleep(1)
    wd.find_element_by_name('password').send_keys(password)
    time.sleep(1)
    wd.find_element_by_class_name('L3NKy   ').click()
    time.sleep(random.randint(3, 4))

#タグ検索し、最新の投稿に移動する
def search(tag):
    address = 'https://www.instagram.com/explore/tags/'
    wd.get(address + tag)
    time.sleep(random.randint(3, 4))
    wd.find_elements_by_class_name('_9AhH0')[10].click()
    time.sleep(random.randint(3, 4))

#いいねを押す
def like():
    global like_cnt
    #例外処理
    try:
        wd.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
        time.sleep(random.randint(3, 4))
        wd.find_element_by_class_name('fr66n').click()
        time.sleep(random.randint(1, 2))
        like_cnt += 1
    except:
        print('エラーが発生しました')
        time.sleep(5)
        return 

if __name__ == '__main__':

    #ユーザ名とパスワード
    username = 'your_username'
    password = 'your_password'

    #タグ設定
    tags = ['l4l','いいね返し','いいねした人で気になった人フォロー','写真好きな人と繋がりたい']

    like_cnt = 0
    begin = datetime.datetime.today()
    tag = random.choice(tags)

    login()
    search(tag)

    #いいね数設定
    while like_cnt < 100:
        like()

    wd.quit()
    end = datetime.datetime.today()

    print('開始時刻：' + str(begin))
    print('終了時刻：' + str(end))
    print('今回のタグは「 ' + tag + ' 」 いいねした数：' + str(like_cnt))