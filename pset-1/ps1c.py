# setting up variables 
annual_salary = float(input('Enter your annual salary: '))
semi_annual_raise = 0.07
annual_investement_return = 0.04
total_cost = 1000000
down_payement = total_cost * 0.25
months_limit = 36 

# check if the salary is sufficient to afford the down payment
cant_afford = False
if annual_salary * 3 < down_payement:
    print('its not possible to pay the down payment in three years')
    cant_afford = True

#bisection implementation
epsilon = 100
high = 10000
low = 0
ans = (high + low) / 2
steps = 0

computed_savings = 0
months = 0
annual_salary_ = annual_salary

while abs(down_payement - computed_savings) >= epsilon:
    if cant_afford == True:
        break

    ans = (high + low) / 2
    computed_savings = 0
    months = 0
    annual_salary_ = annual_salary

    while months < months_limit:
        computed_savings += computed_savings * annual_investement_return / 12
        computed_savings += (ans/10000) * (annual_salary_ / 12)

        if months % 6 == 0 and months != 0: # returns all months that are multiples of 6
            annual_salary_ += annual_salary_ * semi_annual_raise
        
        months += 1 

    if computed_savings > down_payement:
        high = ans
    else: 
        low = ans
    steps += 1

print('Best saving rate:', ans/ 10000)
print('Bisection steps:', steps)
