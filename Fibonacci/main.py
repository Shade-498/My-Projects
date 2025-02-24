def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
  while True:
    num = int(input('Enter a num: '))
    print(fibonacci(num))
    print("-" * 30)  # Divider


if __name__ == "__main__":
  main()