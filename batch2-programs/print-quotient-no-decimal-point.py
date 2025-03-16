#print the quotient of the two numbers without the decimal point

num1 = int(input("Enter the dividend: "))
num2 = int(input("Enter the divisor: "))

if num2 == 0:
    print("Cannot divide by zero.")
else:
    print("The quotient is:", num1 // num2)
