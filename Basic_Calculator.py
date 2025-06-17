#Welcome message
print("Welcome to calculator")
#Take user input if they want to perform calculator Operations or not.
Choice = input ("Do you want to perform calculator operation? Yes/No ")
#The user can enter Yes/ YES/ yeS--To handle this conver the input to lowercase 
Choice = Choice.lower()
#If they type anything other than yes, exit the application
while Choice != "yes":
    print("Please select yes to continue")
    break
else:
#If they type yes, proceed with the application and ask which operation they want to perform
    operation = input("Enter Operation: Addition, Subtraction, Multiplication or Division? ")
    operation = operation.lower()
    expected_operation = ["addition","subtraction","multiplication","division"]
    if operation not in expected_operation:
        print("Invalid Operation") 
#Take operation name and match with expected operation, If match is success proceed for taking numbers
#If the match is not success the tell them its invalid operation
    else:
#Once match is success take Number 1 and Number 2 from user and try converting them to float.
#If it converts to float the proceed further else throw exception to enter a valid number
        Number1 = input("Please enter 1st number ")
        try:
            Number1 = float(Number1)
        except:
            print("Please enter a valid number")
        else:
            Number2 = input("Please enter 2nd number ")
            try:
                Number2 = float(Number2)
            except:
                print("Please enter a valid number")
            else:
#Once Number 1 and 2 is converted define the calculator function with seperate if condition for each operation
                def calculator(a,b):
                    if operation == "addition":
                        result = a + b
                        return round(result,2)
#Round the result to 2 decimal and return the result
                    elif operation == "subtraction":
                        result = a - b
                        return round(result,2)
                    elif operation == "multiplication":
                        result = a*b
                        return round(result,2)
                    elif operation == "division":
                        result = a/b
                        return round(result,2)
                    else:
                        print("Invalid Number")
#Assign the result returned from function to the variable Value and print it.
                Value = calculator(Number1,Number2)
                print (Value)