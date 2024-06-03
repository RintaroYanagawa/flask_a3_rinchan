from flask import request, redirect, url_for, render_template, flash
from holiday import app, db
from holiday.models.mst_holiday import Holiday



@app.route("/list_holiday", methods=["get"])
def list_holiday():
    holidays = Holiday.query.all()
    return render_template("list.html", holidays=holidays)


