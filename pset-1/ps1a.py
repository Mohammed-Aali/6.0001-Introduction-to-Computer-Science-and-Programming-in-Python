# getting input from user
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Entre the precent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream house: '))

# setting up other needed variables
portion_down_payment = total_cost * 0.25        # 25% of the orginal house price
current_savings = 0                             # keep count of the current savings
monthly_salary = annual_salary / 12             # to get how much money per month

months = 0      # counter for how many months till the condition is false
while current_savings < portion_down_payment:
    current_savings += current_savings*(0.04/12)        # adding investement on a monthly basis
    current_savings += portion_saved * monthly_salary   # adding portion saved
    months += 1                                         # incrementing months

print('Number of months', months)

"""
Test Case 1
>>>
Enter your annual salary: 120000
Enter the percent of your salary to save, as a decimal: .10
Enter the cost of your dream home: 1000000
Number of months: 183
>>>
Test Case 2
>>>
Enter your annual salary: 80000
Enter the percent of your salary to save, as a decimal: .15
Enter the cost of your dream home: 500000
Number of months: 105
"""