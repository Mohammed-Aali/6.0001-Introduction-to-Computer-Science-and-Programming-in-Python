# find x such that x**2 - 24 is within epsilon of 0
epsilon = 0.01
k = 24.0
guess = k/2.0
guesses = 0
while(guess*guess - k) >= epsilon:
    guess = guess - ((guess**2) - k)/(2*guess)
    guesses +=1
print('Square root of', k, 'is about', guess)
print(guesses)