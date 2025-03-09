def calculator(choice):
  if choice == 1: # Addition
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Result: ", num1 + num2)
  elif choice == 2: # Subtraction
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Result: ", num1 - num2)
  elif choice == 3: #  Multiplication
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Result: ", num1 * num2)
  elif choice == 4: # Division
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Result: ", num1 / num2)
  elif choice == 5: # Exit
    print("Exiting...")
    exit()


def main():
  while True:
    print("Select an operation: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice(1-5): ")) # User input
    calculator(choice)
    print("=" * 30)

if __name__ == "__main__":
  main()