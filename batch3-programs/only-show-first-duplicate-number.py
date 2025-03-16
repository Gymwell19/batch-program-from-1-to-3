#will only show the first duplicate number in the list from 10 inputs

def display_first_occurrences():
    numbers = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
    seen = set()
    result = []
    
    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    print("Numbers with only the first entry of duplicates:", result)

if __name__ == "__main__":
    display_first_occurrences()
