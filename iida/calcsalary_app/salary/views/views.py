from flask import request, redirect, url_for, render_template, flash, session
from salary import app
import re


@app.route("/")
def input():
    init_val = session.get("input_data", None)
    return render_template("input.html", init_val=init_val)

@app.route('/output', methods=['GET', 'POST'])
def output():
    if request.method == 'POST':
        session["input_data"] = request.form['salary']
        if request.form['salary'] == "":
            flash('給料が未入力です。入力してください')
            return redirect(url_for('input'))
        elif re.fullmatch("[0-9]+", request.form['salary']) == None:
            flash('数字で入力してください')
            return redirect(url_for('input'))
        elif int(request.form['salary']) > 9999999999:
            flash('給与には最大9,999,999,999まで入力可能です。')
            return redirect(url_for('input'))
        elif int(request.form['salary']) < 0 :
            flash('給与にはマイナスの値は入力できません')
            return redirect(url_for('input'))
        else:
            session["input_data"] = None
            input_salary = int(request.form['salary'])
            if input_salary > 1000000:
                tax = round((input_salary -1000000) * 0.2 + 100000)
            else:
                tax = round(input_salary * 0.1)
        
            pay = input_salary - tax
        
            return render_template("output.html", salary=input_salary, pay=pay, tax=tax)
    return redirect(url_for("input"))
