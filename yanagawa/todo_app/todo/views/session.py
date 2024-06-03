from functools import wraps
from flask import request, redirect, url_for, render_template, flash, session
from todo import app
from todo.models.users import Users
import requests


def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login"))
        return view(*args, **kwargs)

    return inner


@app.route("/login", methods=["GET"])
def show_login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    public_id = request.form["public_id"]
    password = request.form["password"]

    user = Users.query.filter_by(public_id=public_id, password=password).first()

    exists_user = user is not None
    if not exists_user:
        return redirect(url_for("show_login"))

    session["logged_in"] = True
    session["logged_userid"] = user.id

    return redirect(url_for("show_list"))


@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    session.pop("logged_userid", None)
    return redirect(url_for("show_hero"))


@app.route("/register", methods=["GET"])
def show_register():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register():
    public_id = request.form["public_id"]
    password = request.form["password"]
    name = request.form["name"]

    response = requests.post(
        "http://127.0.0.1:5000/api/user",
        json={"public_id": public_id, "password": password, "name": name},
    )

    if response.status_code != 200:
        return redirect(url_for("show_register"))

    json = response.json()
    print(json)

    return redirect(url_for("show_login"))
