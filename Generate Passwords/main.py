import random
import string

def generate_password(length: int) -> str:
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password


def main():
    length = int(input('Enter the length of the password: '))
    password = generate_password(length)
    print(f'Generated password: {password}')

if __name__ == '__main__':
    main()