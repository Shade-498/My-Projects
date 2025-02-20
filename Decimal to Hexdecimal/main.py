def decimal_to_hexadecimal(decimal_number):
    hexadecimal_number = hex(decimal_number)[2:]
    return hexadecimal_number

def main():
    while True:
        # Ask the user for input
        user_input = input("Enter a decimal number (or type 'exit' to quit): ")

        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        try:
            # Convert the input to an integer
            decimal_number = int(user_input)

            # Convert the decimal number to hexadecimal
            hexadecimal_number = decimal_to_hexadecimal(decimal_number)

            # Display the result
            print(f"Decimal {decimal_number} in hexadecimal is: {hexadecimal_number}")
        except ValueError:
            # Handle invalid input (non-numeric values)
            print("Error: Please enter a valid decimal number or type 'exit' to quit.")

if __name__ == "__main__":
    main()