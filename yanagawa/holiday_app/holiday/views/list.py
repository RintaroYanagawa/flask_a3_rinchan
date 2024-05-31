from flask import render_template
from holiday import app
from holiday.models.mst_holiday import Holiday


@app.route("/list", methods=["GET"])
def show_list():
    holidays = Holiday.query.order_by(Holiday.holi_date.asc()).all()
    holidays = map(
        lambda holiday: ({"date": holiday.holi_date, "text": holiday.holi_text}),
        holidays,
    )
    return render_template("list.html", holidays=holidays)
