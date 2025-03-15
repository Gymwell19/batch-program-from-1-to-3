#first number divided by the second number

num1 = int(input("Enter the dividend: "))
num2 = int(input("Enter the divisor: "))

if num2 == 0:
    print("Cannot divide by zero.")
else:
    print("The remainder is:", num1 % num2)
1