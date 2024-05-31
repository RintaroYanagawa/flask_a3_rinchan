from flask import request, render_template
from holiday import app


@app.route("/maintenance_date", methods=["GET"])
def show_maintenance_date():
    req = request.args
    message = req.get("msg")
    return render_template("maintenance_date.html", message=message)
