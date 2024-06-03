from flask import Flask
from flask_sqlalchemy import SQLAlchemy




# インスタンス生成
app = Flask(__name__)

# configの有効化
app.config.from_object("holiday.config")

db = SQLAlchemy(app)

from holiday.views import input
from holiday.views import list
from holiday.views import maintenance_date