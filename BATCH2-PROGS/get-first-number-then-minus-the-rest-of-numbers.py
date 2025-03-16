#get first number then minus the sum of the rest of the numbers

numbers = []
for i in range(10):
    numbers.append(float(input(f"Enter number {i+1}: ")))

print(numbers[0] - sum(numbers[1:]))

