from flask import render_template, flash
from holiday import app
from holiday.models.mst_holiday import Holiday
from holiday.utils import get_inform_message


@app.route("/list", methods=["GET"])
def show_list():
    holidays = Holiday.query.order_by(Holiday.holi_date.asc()).all()
    holidays = list(
        map(
            lambda holiday: ({"date": holiday.holi_date, "text": holiday.holi_text}),
            holidays,
        )
    )
    if len(holidays) == 0:
        flash(get_inform_message("I04"), "info")
    return render_template("list.html", holidays=holidays)
