Bank_Balance = 1500
Student_name = "Shiv"
Student_Course = "Python"
Amount_Paid = 1000

while Amount_Paid < 1900:
    if Bank_Balance >= 1000:
        print("Student has paid sufficient amount to unlock the course")
    else:
        print("Student not eligible to unlock the course")
    Amount_Paid = Amount_Paid + 100
    Bank_Balance = Bank_Balance - 100

# BB / Amount paid
# 1500 / 1000
# 1400 / 1100
# 1300 / 1200
# 1200 / 1300
# 1100 / 1400
# 1000 / 1500
# 900 / 1600
# 800 / 1700
# 700 / 1800
# 600 / 1900  ---The programme will not enter the while loop now