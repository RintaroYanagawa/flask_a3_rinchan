from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("todo.config")

db = SQLAlchemy(app)

from todo.views import page, session, user, todo  # noqa: E402

__all__ = ["page", "session", "user", "todo"]
