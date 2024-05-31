# 入力画面の呼び出し

from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday.models.mst_holiday import Holiday

@app.route('/')
def input():
    return render_template('input.html')
