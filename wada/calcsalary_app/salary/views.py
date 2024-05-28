from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP

@app.route("/")
def show_entries():
    return render_template("input.html")

@app.route("/input")
def input():
  input_data = session.get("input_data",None)
  return render_template("input.html",input_data=input_data)


@app.route("/output",methods=["GET","POST"])
def output():
    salary = request.form['salary']
    session["input_data"] = salary
    if request.method == 'POST':
        if salary == "":
            flash("給与が未入力です。入力してください")
            return redirect(url_for("input"))
        elif len (salary)>11:
            flash("給与には最大9,999,999,999まで入力可能です。")
            return redirect(url_for("input"))
        elif int(salary)<0:
            flash("給与にはマイナスの値は入力できません。")
            return redirect(url_for("input"))
        else:
            salary = int(request.form['salary'])
            price=0
            tax=0
            if salary > 1000000:
                tax = 100000 + (salary-1000000)*0.2
                price = salary - tax
            else:
                tax = salary*0.1
                tax = Decimal(int(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
                price = salary - tax
 
            return render_template("output.html",salary=salary,price=price,tax=tax)
    return redirect('/input')
  

