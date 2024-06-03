from flask import request, redirect, url_for, render_template, flash, session
from dental import app
from functools import wraps

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        if request.form["username"] != app.config["USERNAME"]:
            flash("ユーザー名が異なります")
        elif request.form["password"] != app.config["PASSWORD"]:
            flash("パスワードが異なります")
        else:
            session["logged_in"]=True
            flash("ログインしました")
            return render_template("reserve.html")
    return render_template("login.html")