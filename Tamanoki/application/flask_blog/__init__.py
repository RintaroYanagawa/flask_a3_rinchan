# Flask自体をインポートする
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flaskのアプリケーション本体を作成
# from_object 設定を読み込むためのメゾット
app = Flask(__name__)
app.config.from_object('flask_blog.config')

db = SQLAlchemy(app)

# これから作成するviewsというファイルにインポートする
from flask_blog.views import views,entries