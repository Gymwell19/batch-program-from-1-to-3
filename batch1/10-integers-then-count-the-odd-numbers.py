#Counted of odd numbers

odd_count = 0
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 != 0:
        odd_count += 1

print("Number of odd numbers:", odd_count)

#result of the odd numbers from 10 input numbers