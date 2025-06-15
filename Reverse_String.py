Input_string = input("Please enter a value to reverse:")
print (Input_string)
def reversestring(Input_string):
    reversedresult= ''
    for i in Input_string:
      reversedresult = i+reversedresult
    return reversedresult


print("The reversed value is", reversestring(Input_string))