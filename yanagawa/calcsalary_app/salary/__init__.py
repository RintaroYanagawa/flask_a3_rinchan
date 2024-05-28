from flask import Flask

app = Flask(__name__)

import salary.views.views  # noqa: E402

app.config.from_object("salary.config")

__all__ = ["salary"]
