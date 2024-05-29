from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP


@app.route("/", methods=["GET", "POST"])
def input():
    input_data = session.get("input_data",None)
    return render_template("input.html",input_data = input_data)


@app.route("/output", methods=["GET", "POST"])
def output():
    if request.method == "POST":
        input_salary = request.form['salary']
        session["input_data"] = input_salary
        if input_salary =="":
            flash("給与が未入力です。入力してください。")
            return redirect (url_for('input'))
        elif int(input_salary) > 1000000000:
            flash("給与には最大9,999,999まで入力可能です")
            return redirect (url_for('input'))
        elif int(input_salary) < 0:
            flash("給与にはマイナスの値が入力できません")
            return redirect (url_for('input'))
        
        else:
            input_salary = int(input_salary)
            session["input_data"] = ""
      
        

            input_salary = int(request.form["salary"])
            allowance,tax = calcsalary(input_salary)
            "{:,}".format(input_salary)
            return render_template("output.html", salary=input_salary, allowance=allowance, tax=tax)


def calcsalary(salary):
    allowance = 0
    tax = 0

    if salary > 1000000:
        tax = (salary - 1000000) * 0.2 + 1000000 * 0.1
        tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
        allowance = salary - tax

    else:
        tax = salary * 0.1
        tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
        allowance = salary - tax

    return allowance, tax
