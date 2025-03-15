#a list of numbers from 0 to 100 that do not end in 0 or 5

numbers = [num for num in range(101) if num % 10 not in [0, 5]]
print(numbers)
