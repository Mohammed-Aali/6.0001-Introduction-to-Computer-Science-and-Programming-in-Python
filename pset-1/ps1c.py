while True:
    try:
        annual_salary = float(input('Enter your annual salary: '))
        break
    except ValueError:
        print('Type float or integers')

semi_annual_raise = 0.07
investment_annual_returns = 0.04
down_payment = 0.25 * total_cost

months = 36


monthly_salary = annual_salary / 12

epsilon = 100
high = 10000
low = 0
guess = (high + low) / 2

percentage = guess / 10000
per_month = percentage * monthly_salary 
per_three_years = per_month * 36

bisection = 0
if annual_salary * 3 < 250000:
    print('The down payment cannot be paid given three years')
else:
    while abs(per_three_years - (250000)) >= 100.0:
        if per_three_years > 250000:
            high = guess
        else:
            low = guess
        guess = (high + low) / 2
        percentage = guess / 10000
        per_three_years = (percentage * monthly_salary) * 36
        bisection +=1
    print('Best saving rate:', percentage)
    print('bisection steps:', bisection)
    



    