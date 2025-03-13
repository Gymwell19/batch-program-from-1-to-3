#numbers ranging from 1-100 excluding of 0
numbers = [num for num in range(101) if num % 10 != 0]
print(numbers)