from flask import request, redirect, url_for, render_template, flash,session
from salary import app
from decimal import Decimal, ROUND_HALF_UP


@app.route("/",methods=['GET','POST'])
def input():
    input_data = session.get('input_data',None)
    return render_template("input.html", input_data = input_data)



@app.route('/output', methods=['GET', 'POST'])
def add():
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
    
def calcsalary(sa):
    if sa<=1000000:
        tax =sa * 0.1
    else:
        tax =100000 + (sa-1000000)*0.2
    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    pay = sa - tax
    return pay,tax


