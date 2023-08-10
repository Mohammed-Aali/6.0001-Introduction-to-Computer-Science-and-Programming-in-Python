x = 9
ans = 0

iters_left = x
while(iters_left != 0):
    ans = ans + x
    iters_left -= 1

print(str(x) + "*" + str(x) + ' = ' + str(ans))