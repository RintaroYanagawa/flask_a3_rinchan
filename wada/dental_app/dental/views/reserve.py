# データベース処理、そのあとの結果画面の呼び出し
from flask import request, redirect, url_for, render_template, flash, session
from dental import app
from dental.models.mst_dental import Dental
from dental import db

@app.route("/reserve", methods=['POST', 'GET'])
def reserve():
    reserve_num= request.form['reserve_num']
    reserve_name = request.form['reserve_name']
    reserve_date = request.form['reserve_date']
    reserve_time = request.form['reserve_time']

    #普通に登録
    dentals = Dental.query.get(reserve_num)
    if dentals is None:
        new_reserve = Dental(
            number=reserve_num,
            name=reserve_name,
            date=reserve_date,
            reservetime=reserve_time
        )
        db.session.add(new_reserve)
        db.session.commit()
        flag = 1
    #更新か削除
    else:
        if request.form["button"] == "insert_update":
            update_reserve = Dental(
                number=reserve_num,
                name=reserve_name,
                date=reserve_date,
                reservetime=reserve_time
            )
            db.session.merge(update_reserve)
            db.session.commit()
            flag = 2
        elif request.form["button"] == "delete":
            db.session.delete(dentals)
            db.session.commit()
            flag = 3
        elif request.form["button"] == "confirm":
            reservation = Dental.query.filter_by(number=reserve_num).first()
            reserve_date = reservation.date
            reserve_time = reservation.reservetime
            flag = 4
    return render_template(
        'result.html',
        date = reserve_date,
        time = reserve_time,
        flag = flag)
