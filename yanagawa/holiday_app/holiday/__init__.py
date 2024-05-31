from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("holiday.config")

db = SQLAlchemy(app)

from holiday.views import input, maintenance_date, list  # noqa: E402

__all__ = ["input", "maintenance_date", "list"]
