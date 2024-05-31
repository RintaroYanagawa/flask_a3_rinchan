from flask import render_template
from holiday import app

@app.route("/", methods=["GET", "POST"])
def input():
    return render_template("input.html")



