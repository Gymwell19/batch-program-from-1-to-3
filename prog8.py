#Counted of odd numbers
numbers = (map(int, input("enter 10 numbers:").split()))
print(sum(1 for num in numbers if num % 2!=0))