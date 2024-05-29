def validate_salary(input_salary):
    if input_salary is None:
        return {"ok": False, "type": "MissingInputError"}
    if input_salary > 9999999999:
        return {"ok": False, "type": "MaxValueExceededException"}
    if input_salary < 0:
        return {"ok": False, "type": "NegativeValueError"}
    return {"ok": True, "type": None}


def calc_salary(input_salary):
    threshold = 1000000

    base_salary = min(input_salary, threshold)
    extra_salary = max(0, input_salary - threshold)

    salary_tax_amount = round(base_salary * 0.1)
    extra_tax_amount = round(extra_salary * 0.2)

    tax_amount_sum = salary_tax_amount + extra_tax_amount

    pay_amount = input_salary - tax_amount_sum

    return pay_amount, tax_amount_sum
