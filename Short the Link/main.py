import pyshorteners

def shorten_url(long_url):
    shortener = pyshorteners.Shortener() # Create an instance of the Shortener class
    short_url = shortener.tinyurl.short(long_url) # Use the short() method to shorten the URL
    return short_url

def main():
    print("Programm for shortening links")
    long_url = input("Enter your long link: ")

    try:
        short_url = shorten_url(long_url) # Short the URL
        print(f"Shorten link: {short_url}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()