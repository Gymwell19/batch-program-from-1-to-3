#a program that checks for duplicates in a list of numbers and displays "Duplicate" if the number is already in the list and "Unique" if the number is not in the list. If the input is not a number, the program will display "Invalid input. Please enter a valid integer."
def check_duplicates():
    entered_numbers = []
    
    while True:
        try:
            num = int(input("Enter a number: "))
            if num in entered_numbers:
                print("Duplicate")
            else:
                print("Unique")
                entered_numbers.append(num)

#have to put this code for this to work
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    check_duplicates()
