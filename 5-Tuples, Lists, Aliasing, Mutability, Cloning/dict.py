month_numbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5,
1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}
print('The third month is ' + month_numbers[3])
dist = month_numbers['Apr'] - month_numbers['Jan']
print('Apr and Jan are', dist, 'months apart')

print(month_numbers.keys())