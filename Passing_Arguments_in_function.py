'''
def joinnumb(*num):
    addednumb = 0
    for i in num:
        addednumb = addednumb + i
    print ("Sum of number is:", addednumb)

'''
def joindata(rollno, **data):
    print (rollno)
    for i,j in data.items():
        print (i,j)


joindata(25, Name = "Shiv", Age = 55, Rank = 2)