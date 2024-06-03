from flask import request, redirect, url_for, render_template, flash
from holiday import app, db
from holiday.models.mst_holiday import Holiday


@app.route("/maintenance_date", methods=["post"])
def maintenance_date():
    # バリデーション
    if request.form['holiday'] == "":
        flash("祝日日付を入力してください")
        return redirect(url_for("show_entries"))
    elif  0 < len(request.form['holiday_text']) or len(request.form['holiday_text']) <=20:
        flash("祝日テキストは1文字以上20文字以下で入力してください")
        return redirect(url_for("show_entries"))

    if request.form["button"] == "insert_update":
        holiday = Holiday.query.get(request.form["holiday"])
        if holiday is not None: # holidayがデータベースに存在しているときは更新
            holiday = Holiday(
                holi_date=request.form["holiday"],
                holi_text=request.form["holiday_text"]
            )
            db.session.merge(holiday)
            db.session.commit()
            holi_date = holiday.holi_date
            holi_text = holiday.holi_text
            flag = "更新"
            return render_template("result.html", holi_date=holi_date, holi_text=holi_text, flag=flag)
        else: # holidayがデータベースに存在していないときは新規作成
            holiday = Holiday(
                holi_date=request.form["holiday"],
                holi_text=request.form["holiday_text"]
            )
            db.session.add(holiday)
            db.session.commit()
            holi_date = holiday.holi_date
            holi_text = holiday.holi_text
            flag = "新規登録"
            return render_template("result.html", holi_date=holi_date, holi_text=holi_text, flag=flag)


    elif request.form["button"] == "delete": # 削除ボタンを押したら削除
        holiday = Holiday.query.get(request.form["holiday"])
        if holiday is not None:
            holiday = Holiday.query.get(request.form["holiday"])
            holi_date = holiday.holi_date
            holi_text = holiday.holi_text
            db.session.delete(holiday)
            db.session.commit()
            flag = "削除"
            return render_template("result.html", holi_date=holi_date, holi_text=holi_text, flag=flag)  
        else:
            flash(str(request.form["holiday"]) + "は、祝日マスタに登録されていません")
            return redirect(url_for("show_entries"))