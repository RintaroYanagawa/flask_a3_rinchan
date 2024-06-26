from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# インスタンス生成
app = Flask(__name__)

# configの有効化
app.config.from_object("flask_blog.config")

db = SQLAlchemy(app)
from flask_blog.views import views, entries
