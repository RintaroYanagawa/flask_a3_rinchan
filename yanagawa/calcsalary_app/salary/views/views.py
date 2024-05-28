from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from salary.utils.salary import calc_salary, validate_salary


@app.route("/")
def input():
    input_salary = session.get("input_salary")
    return render_template("input.html", salary=input_salary)


@app.route("/output", methods=["GET", "POST"])
def output():
    if request.method != "POST":
        return redirect(url_for("input"))

    error_message_master = {
        "MissingInputError": "給与が未入力です。入力してください。",
        "MaxValueExceededException": "給与には最大9,999,999,999まで入力可能です。",
        "NegativeValueError": "給与にはマイナスの値は入力できません。",
    }

    input_salary = request.form["salary"]
    session["input_salary"] = input_salary
    salary = int(input_salary) if input_salary != "" else None
    result = validate_salary(salary)
    if not result["ok"]:
        flash(error_message_master[result["type"]])
        return redirect(url_for("input"))

    pay_amount, tax_amount = calc_salary(salary)

    session["input_salary"] = ""

    return render_template(
        "output.html", salary=salary, pay_amount=pay_amount, tax_amount=tax_amount
    )
