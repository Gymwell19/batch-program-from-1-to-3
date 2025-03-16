#get the lowest number from the user input
#continue to ask for a number until an ivalid input is entered

def find_lowest_number():
    lowest = None
    
    while True:
        try:
            num = int(input("Enter a number: "))
            if lowest is None or num < lowest:
                lowest = num
#this is the code that to use fo it to work       
        except ValueError:
            print(f"Invalid input. The lowest number entered was: {lowest}")
            break

if __name__ == "__main__":
    find_lowest_number()

