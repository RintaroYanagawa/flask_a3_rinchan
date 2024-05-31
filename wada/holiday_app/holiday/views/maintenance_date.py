# データベース処理、そのあとの結果画面の呼び出し

from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday.models.mst_holiday import Holiday
from holiday import db

@app.route('/maintenance_date', methods=['POST', 'GET'])
def update_holiday():
    holiday_date = request.form['holiday']
    holiday_text = request.form['holiday_text']

    #普通に登録
    holiday = Holiday.query.get(holiday_date)
    if holiday is None:
        new_holiday = Holiday(
            holi_date=holiday_date,
            holi_text=holiday_text
        )
        db.session.add(new_holiday)
        db.session.commit()
        flag = 1
    #更新か削除
    else:
        if request.form["button"] == "insert_update":
            update_holiday = Holiday(
            holi_date=holiday_date,
            holi_text=holiday_text
            )
            db.session.merge(update_holiday)
            db.session.commit()
            flag = 2
        elif request.form["button"] == "delete":
            db.session.delete(holiday)
            db.session.commit()
            flag = 3
    return render_template(
        'result.html',
        holiday_date=holiday_date,
        holiday_text=holiday_text,
        flag = flag)