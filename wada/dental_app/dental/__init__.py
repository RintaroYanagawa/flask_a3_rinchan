from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("dental.config")

db = SQLAlchemy(app)

from dental.views import start,login,reserve