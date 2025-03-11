import datetime

def time_and_date():
    now = datetime.datetime.now() # Current time and date
    return now.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    print(time_and_date())