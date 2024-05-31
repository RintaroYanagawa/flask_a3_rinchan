from flask import request, render_template
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Entry


@app.route('/maintenance_data', methods=['POST'])
def maintenance_data():
    entry = Entry(
        holi_date=request.form['holiday'],
        holi_text=request.form['holiday_text']
    )
    db.session.add(entry)
    db.session.commit()
    return render_template ("reult.html")