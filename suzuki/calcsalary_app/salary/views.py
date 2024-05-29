from flask import request, redirect, url_for, render_template, flash,session
from salary import app
from decimal import Decimal, ROUND_HALF_UP


@app.route("/",methods=['GET','POST'])
def input():
    input_data = session.get('input_data',None)
    return render_template("input.html", input_data = input_data)


@app.route('/output',methods=['GET','POST'])
def output():
    input_salary = request.form['salary']
    session["input_data"] = input_salary
    if input_salary == "":
        flash('給与が未入力です')
        return redirect(url_for('input'))
    elif int(input_salary) < 0:
        flash('給与にはマイナスの値は入力できません。')
        return redirect(url_for('input'))
    elif len(input_salary) >= 11:
        flash('給与には9,999,999,999まで入力可能です。')
        return redirect(url_for('input'))
    else:
        session["input_data"] = ""
        input_salary = int(input_salary)
        pay,tax = calcsalary(input_salary)
        return render_template("output.html", salary=input_salary, pay=pay, tax=tax)
    
def calcsalary(sa):
    if sa<=1000000:
        tax =sa * 0.1
    else:
        tax =100000 + (sa-1000000)*0.2
    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    pay = sa - tax
    return pay,tax


