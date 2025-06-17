def Fibonacci(steps):
    if steps == 0:
        return 0
    elif steps == 1:
        return 1
    else:
        Numb1 = 0
        Numb2 = 1
        for i in (steps):
            Numb3= Numb1 + Numb2
            Numb1 = Numb2
            Numb2 = Numb3
        return Numb2

for i in range(5,8):
    print (Fibonacci(i))