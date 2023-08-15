x = 25
epsilon = 0.01
step = epsilon**2
num_guess = 0
ans = 0.0

while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    num_guess += 1

print('num_guess=', num_guess)

if abs(ans**2 - x) >= epsilon:
    print('Failed on square root of', x)
else:
    print(ans, 'is Close to square root of', x)