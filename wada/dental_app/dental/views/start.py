# 初期画面

from flask import request, redirect, url_for, render_template, flash, session
from dental import app
from dental.models.mst_dental import Dental

@app.route('/')
def home():
    return render_template("start.html")
