def decimal_to_hexadecimal(decimal_number):
    # Проверка на неотрицательное число
    if decimal_number < 0:
        return "Enter proper number."

    # Определяем символы, используемые в шестнадцатеричной системе
    hex_chars = "0123456789ABCDEF"
    hexadecimal_number = ""

    # Специальный случай нуля
    if decimal_number == 0:
        return "0"

    while decimal_number > 0:
        remainder = decimal_number % 16  # Остаток от деления на 16
        hexadecimal_number = hex_chars[remainder] + hexadecimal_number  # Добавляем соответствующий символ
        decimal_number //= 16  # Целочисленное деление на 16

    return hexadecimal_number


# Ввод числа от пользователя
try:
    decimal_number = int(input("Enter decimal number: "))
    result = decimal_to_hexadecimal(decimal_number)
    print(f"Result: {result}")
except ValueError:
    print("Enter correct number.")