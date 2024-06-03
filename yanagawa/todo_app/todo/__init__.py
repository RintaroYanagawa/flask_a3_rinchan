from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("todo.config")

db = SQLAlchemy(app)

from todo.views import user  # noqa: E402

__all__ = ["user"]
