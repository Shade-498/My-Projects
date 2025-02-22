def is_leap_year(year: int) -> bool:
    # A leap year is divisible by 4 but not by 100, unless it's also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    while True:
        user_input = input("Enter a year (or type 'exit' to quit): ") # Ask the user for input
        
        if user_input.lower() == 'exit': # Check if the user wants to exit
            print("Exiting the program. Goodbye!")
            break

        year = int(user_input) # Convert the input to an integer

        if is_leap_year(year): # Check if the year is a leap year and display the result
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")

if __name__ == "__main__":
    main()