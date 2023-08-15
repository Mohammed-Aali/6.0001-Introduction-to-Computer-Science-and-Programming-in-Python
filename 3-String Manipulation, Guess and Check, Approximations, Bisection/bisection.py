x = -27
if x < 0:
    negative = True
    x *= -1

epsilon = 0.01
num_guesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/ 2.0


while abs(ans**3 - x) >= epsilon:
    print('low=', low, 'high=', high, 'ans=', ans)
    num_guesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
    
print('num_guesses=', num_guesses)