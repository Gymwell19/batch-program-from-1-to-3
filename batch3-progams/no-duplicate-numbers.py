#print numbers without the duplicate from 10 inpits

def display_unique_numbers():
    numbers = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
    unique_numbers = [num for num in numbers if numbers.count(num) == 1]
    print("Numbers without duplicates:", unique_numbers)

if __name__ == "__main__":
    display_unique_numbers()


