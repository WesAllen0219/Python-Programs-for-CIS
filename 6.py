def get_number_of_entries():
    while True:
        try:
            num_entries = int(input("Specify your number of entries to be added to a total"))
            if num_entries > 0:
                return num_entries
            else:
                print("Please enter a positive integer for the number of entries.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
def get_numbers(num_entries):
    numbers = []
    for i in range(1, num_entries + 1):
        while True:
            try:
                number = float(input(f"Enter numerical value {i}: "))
                numbers.append(number)
                break
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
    return numbers
def calculate_running_total(numbers):
    total = 0
    print("\nRunning Total Updates:")
    for i, number in enumerate(numbers, start=1):
        print(f"pass#{i} Running Total is {total} - Running total before adding is {total}")
        total += number
        print(f"pass#{i} Running Total is {total} - Running total after adding is {total}")
    return total
def display_results(num_entries, numbers, total):
    print("\nSummary:")
    print(f"You requested to add {num_entries} numbers to calculate a running total.")
    print("Your entries were:", ', '.join(map(str, numbers)))
    print("Your final total is:", total)
def main():
    num_entries = get_number_of_entries()
    numbers = get_numbers(num_entries)
    total = calculate_running_total(numbers)
    display_results(num_entries, numbers, total)
if __name__ == "__main__":
    main()