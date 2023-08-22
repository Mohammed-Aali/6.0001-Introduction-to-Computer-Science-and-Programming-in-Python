# setting up variables 
annual_salary = float(input('Enter your annual salary: '))
semi_annual_raise = 0.07                # semi-annual raise amount
monthly_investement_return = 0.04 / 12  # monthly investement returns
total_cost = 1000000                    # total cost of the house
down_payment = total_cost * 0.25       # down_payment is 25% of total cost of the house. "250000"
months_limit = 36                       # three years

# check if the salary is sufficient to afford the down payment
cant_afford = False
if annual_salary * 3 < down_payment:
    cant_afford = True

#bisection implementation
epsilon = 100               #margin of error. the saved amount needs to be within 100 range
high = 10000                # the highest possible value for bisection
low = 0                     # the lowest possible value for bisection
ans = (high + low) / 2.0


computed_savings = 0
steps = 0


while abs(computed_savings - down_payment) > epsilon:
    if cant_afford == True:
        break

    ans = (high + low) / 2.0
    computed_savings = 0
    months = 0
    annual_salary_ = annual_salary

    while months < months_limit:
        computed_savings += computed_savings * monthly_investement_return
        computed_savings += (ans / 10000) * (annual_salary_ / 12)

        if months % 6 == 0 and months != 0: # returns all months that are multiples of 6
            annual_salary_ += annual_salary_ * semi_annual_raise
        months += 1 

    if computed_savings > down_payment:
        high = ans
    else: 
        low = ans
    steps += 1

if cant_afford == True:
    print('its not possible to pay the down payment in three years')
else:
    print('Best saving rate:', round((high + low) / 2))
    print('Bisection steps:', steps)
