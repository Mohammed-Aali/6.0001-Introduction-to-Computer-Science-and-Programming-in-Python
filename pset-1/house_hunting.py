annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the precent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream house: '))
semi_annual_raise = float(input('Enter your semi-annual raise, as a decimal: '))

portion_down_payment = 0.25
current_savings = 0

money_needed = portion_down_payment * total_cost 
# r is annual return of investment
r = 0.04

semi_annual_raise_month = 6
months = 0
while(current_savings < money_needed):
    current_savings += current_savings*r/12 
    current_savings += (annual_salary/12) * portion_saved

    if semi_annual_raise_month == months:
        annual_salary += annual_salary*semi_annual_raise
        semi_annual_raise_month += 6

    months+=1

print('Number of months:',months)
print('Current savings:', current_savings)
