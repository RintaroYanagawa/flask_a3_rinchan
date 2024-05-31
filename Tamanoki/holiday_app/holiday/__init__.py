# Flask自体をインポートする
from flask import Flask

# SQLAlchemyライブラリをインストールする
from flask_sqlalchemy import SQLAlchemy


# Flaskのアプリケーション本体を作成
# from_object 設定を読み込むためのメゾット
app = Flask(__name__)
app.config.from_object('holiday.config')

# 他のプログラムはdbという変数を参照することでデータベースを扱うことができるようになる
db = SQLAlchemy(app)

from holiday.views import input