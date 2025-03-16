#program that ask numbers then display the numbers from lowest to highest after invalid input 

def sort_numbers():
    numbers = []
    
    while True:
        try:
            num = int(input("Enter a number: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input. Sorting and displaying the numbers...")
            break

 #will sort the numbers from lowest to highest   
    numbers.sort()
    print("Numbers from lowest to highest:", numbers)

if __name__ == "__main__":
    sort_numbers()

