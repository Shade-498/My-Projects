import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0  # Counter to track the number of attempts
    max_attempts = 10  # Maximum number of attempts allowed

    print(f"Welcome, I'm thinking of a number between 1 and 100. You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        attempts += 1  # Increment the attempt counter

        if guess < secret_number:
            print(f"Too low! Try again. Attempts left: {max_attempts - attempts}")
            print('-' * 30)  # Divider

        elif guess > secret_number:
            print(f"Too high! Try again. Attempts left: {max_attempts - attempts}")
            print('-' * 30)  # Divider
            
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            return

    # If the user runs out of attempts, reveal the secret number
    print(f"Sorry, you've run out of attempts. The number was {secret_number}.")

if __name__ == "__main__":
  guess_the_number()