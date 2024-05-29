# Flask自体をインポートする
from flask import Flask

# Flaskのアプリケーション本体を作成
# from_object 設定を読み込むためのメゾット
app = Flask(__name__)
app.config.from_object('salary.config')


# これから作成するviewsというファイルにインポートする
import salary.views