from flask import request, redirect, url_for, render_template, flash, jsonify
from todo import app, db


@app.route("/")
def show_hero():
    return render_template("hero.html")
