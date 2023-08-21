# getting input from user
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Entre the precent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream house: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

# setting up other needed variables
portion_down_payment = total_cost * 0.25        # 25% of the orginal house price
current_savings = 0                             # keep count of the current savings

months = 0      # counter for how many months till the condition is false
while current_savings < portion_down_payment:
    current_savings += current_savings*0.04/12                  # adding investement on a monthly basis
    current_savings += portion_saved * (annual_salary / 12)     # adding portion saved and updating the monthly salary by calculating the new annual salary
    # part b implementation
    if months % 6 == 0 and months != 0: # returns all months that are multiples of 6
        annual_salary += annual_salary * semi_annual_raise
    
    months += 1                                                 # incrementing months

print('Number of months', months)
"""
Test Case 1
>>>
Enter your starting annual salary: 120000
Enter the percent of your salary to save, as a decimal: .05
Enter the cost of your dream home: 500000
Enter the semiannual raise, as a deci mal: .03
Number of months: 142
>>>
Test Case 2
>>>
Enter your starting annual salary: 80000
Enter the percent of your salary to save, as a decimal: .1
Enter the cost of your dream home: 800000
Enter the semiannual raise, as a deci mal: .03
Number of months: 159
>>>
Test Case 3
>>>
Enter your starting annual salary: 75000
Enter the percent of your salary to save, as a decimal: .05
Enter the cost of your dream home: 1500000
Enter the semiannual raise, as a deci mal: .05
Number of months: 261
"""
