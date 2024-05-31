from flask import request, redirect, url_for, render_template, flash, session
from holiday import app, db
from holiday.models.mst_holiday import Holiday
from holiday.utils import get_inform_message


@app.route("/", methods=["GET"])
def show_input_date():
    return render_template("input.html")


@app.route("/date/upsert", methods=["POST"])
def upsert_date():
    date = request.form["holiday"]
    exists_holiday = Holiday.query.get(date) is not None
    if exists_holiday:
        return redirect(url_for("update_date"), code=307)
    else:
        return redirect(url_for("create_date"), code=307)


@app.route("/date/create", methods=["POST"])
def create_date():
    date = request.form["holiday"]
    text = request.form["holiday_text"]
    holiday = Holiday(holi_date=date, holi_text=text)
    db.session.add(holiday)
    db.session.commit()
    message = get_inform_message("I01", date, text)
    return redirect(url_for("show_maintenance_date", msg=message))


@app.route("/date/update", methods=["POST"])
def update_date():
    date = request.form["holiday"]
    text = request.form["holiday_text"]
    holiday = Holiday(holi_date=date, holi_text=text)
    db.session.merge(holiday)
    db.session.commit()
    message = get_inform_message("I02", date, text)
    return redirect(url_for("show_maintenance_date", msg=message))


@app.route("/date/delete", methods=["POST"])
def delete_date():
    date = request.form["holiday"]
    text = request.form["holiday_text"]
    holiday = Holiday.query.get(date)
    if holiday is None:
        flash(get_inform_message("I04"))
        return redirect(url_for("show_input_date"))
    db.session.delete(holiday)
    db.session.commit()
    message = get_inform_message("I03", date, text)
    return redirect(url_for("show_maintenance_date", msg=message))
