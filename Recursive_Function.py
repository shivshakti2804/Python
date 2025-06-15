def Fibonacci(steps):
    if steps == 0:
        return 0
    elif steps == 1:
        return 1
    else:
        return Fibonacci(steps - 1) + Fibonacci(steps - 2)

for i in range(0,8):
    print (Fibonacci(i))