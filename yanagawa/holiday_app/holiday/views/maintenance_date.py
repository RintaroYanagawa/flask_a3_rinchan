from flask import render_template
from holiday import app


@app.route("/maintenance_date", methods=["GET"])
def show_maintenance_date():
    return render_template("maintenance_date.html")
