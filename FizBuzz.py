def Fibuzz(Numb):
    if Numb%3 == 0 and Numb%5 == 0:
        return "FizzBuzz"
    elif Numb%5 == 0:
        return "Buzz"
    elif Numb%3 == 0 :
        return "Fizz"
    else:
        return Numb

for i in range(1,101):
    print(Fibuzz(i))