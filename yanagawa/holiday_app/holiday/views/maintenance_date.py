from flask import request, redirect, url_for, render_template, flash, session
from holiday import app, db
from holiday.models.mst_holiday import Holiday


@app.route("/maintenance_date", methods=["GET"])
def show_maintenance_date():
    req = request.args
    message = req.get("msg")
    return render_template("maintenance_date.html", message=message)
