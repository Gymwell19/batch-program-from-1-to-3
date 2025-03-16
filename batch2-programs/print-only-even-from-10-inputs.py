#ten inputs then get the even

even_count = 0
even_numbers = []

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        even_count += 1
        even_numbers.append(num)

print("Number of even numbers:", even_count)
print("The even numbers are:", even_numbers)
1