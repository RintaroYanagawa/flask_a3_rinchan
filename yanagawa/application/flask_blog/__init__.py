from flask import Flask

app = Flask(__name__)

import flask_blog.views  # noqa: E402

app.config.from_object("flask_blog.config")

__all__ = ["flask_blog"]
