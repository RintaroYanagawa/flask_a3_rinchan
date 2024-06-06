from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from holiday import app
from holiday.models.mst_holiday import Holiday




@app.route('/list', methods=['POST'])
def index():
    if request.form['button'] == "list":
        holiday_list = Holiday.query.all()
        return render_template('list.html',holiday_list=holiday_list )