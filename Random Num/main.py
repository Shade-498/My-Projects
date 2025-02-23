import random

# Generate a random number between x and y
x = int(input("Enter a 1st number: "))
y = int(input("Enter a 2nd number: "))
# Result
res = random.randint(x, y)

if __name__ == "__main__":
    print(f'Random number between {x} and {y} is {res}')