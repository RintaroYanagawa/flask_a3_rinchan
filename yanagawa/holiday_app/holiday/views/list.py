from flask import request, redirect, url_for, render_template, flash, session
from holiday import app, db
from holiday.models.mst_holiday import Holiday
from holiday.utils import get_inform_message


@app.route("/list", methods=["GET"])
def show_list():
    holidays = Holiday.query.order_by(Holiday.holi_date.asc()).all()
    holidays = map(
        lambda holiday: ({"date": holiday.holi_date, "text": holiday.holi_text}),
        holidays,
    )
    return render_template("list.html", holidays=holidays)
