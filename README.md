# instabot
An instagram bot developed in Python with Selenium that helps you get more Instagram followers.
## Install
You’ll need to have:

 - [Python](https://www.python.org/downloads/)
 - [Selenium](https://selenium-python.readthedocs.io/installation.html)
 - [Google Chrome](https://www.google.com/chrome/)
 - [Chromedriver](https://chromedriver.chromium.org/downloads)

Go check them out if you don't have them locally installed.

If you have correctly downloaded Chromedriver,try adding Chromedriver location to your PATH system environment variable.

## Usage

Open **main.py** , you’ll have to change some lines.

1. Change your_username and your_password to your Instagram credentials.
```
#ユーザ名とパスワード
username = 'your_username'
password = 'your_password'
```
2. Change this line with your custom tags.
```
#タグ設定
tags = ['l4l','いいね返し','いいねした人で気になった人フォロー','写真好きな人と繋がりたい']
```
3. In order to keep your account safe and not locked out, you should be satisfied with less than 500 likes per day.
```python
#いいね数設定
while  like_cnt < 100:
	like()
```
4. Run
```
python main.py
```
## Author
ZHOU ZHUOQIAO

## License

MIT License
