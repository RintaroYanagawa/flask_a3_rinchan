from flask import Flask

# インスタンス生成
app = Flask(__name__)

# configの有効化
app.config.from_object("flask_blog.config")

import flask_blog.views
