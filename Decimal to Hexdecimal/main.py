def decimal_to_hexadecimal(decimal_number):

    # Hex nums
    hex_chars = "0123456789ABCDEF"
    hexadecimal_number = ""

    # If negative
    if decimal_number < 0:
        return "Enter proper number."

    # If zero
    if decimal_number == 0:
        return "0"

    while decimal_number > 0:
        remainder = decimal_number % 16
        hexadecimal_number = hex_chars[remainder] + hexadecimal_number
        decimal_number //= 16

    return hexadecimal_number


# User input
try:
    decimal_number = int(input("Enter decimal number: "))
    result = decimal_to_hexadecimal(decimal_number)
    print(f"Result: {result}")
except ValueError:
    print("Enter correct number.")