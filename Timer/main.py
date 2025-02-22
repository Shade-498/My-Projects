from datetime import datetime, timedelta

def countdown(target_date: datetime) -> str:
    now = datetime.now()

    # Calculate the difference between the target date and the current time
    time_left = target_date - now

    # Extract days, hours, minutes, and seconds from the time difference
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)  # 1 hour = 3600 seconds
    minutes, seconds = divmod(remainder, 60)  # 1 minute = 60 seconds

    return f"Time left: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

# Example usage
def main():
    target = datetime(2025, 12, 31, 23, 59, 59) # New Year 2026
    print(countdown(target))

if __name__ == "__main__":
    main()