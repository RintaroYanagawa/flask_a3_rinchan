from flask import request, redirect, url_for, render_template, flash, session
from holiday import app, db
from holiday.models.mst_holiday import Holiday
# from holiday.views.views import login_required



@app.route('/maintenance_date', methods=['POST'])
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
   

    else:
        if request.form['button'] == "insert_update":
            update_holiday = Holiday(
            holi_date=holiday_date,
            holi_text=holiday_text
            )
            db.session.merge(update_holiday)
            db.session.commit()
            return redirect(url_for('result.html'))
            flag = 2

        elif request.form['button'] == "delete":
            delete_holiday = Holiday(
            holi_date=holiday_date,
            holi_text=holiday_text
            )
            db.session.delete(delete_holiday)
            db.session.commit()
            return redirect(url_for('result.html'))
            flag = 3
    return render_template('result.html',holiday_date=holiday_date, holiday_text=holiday_text, flag=flag)
                




    
