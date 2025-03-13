import time

def calculate_accuracy(user_text, original_text):
    correct_chars = sum(1 for a, b in zip(original_text, user_text) if a == b)
    accuracy = (correct_chars / len(original_text)) * 100
    return accuracy


def calculate_speed(start_time, end_time, text):
    elapsed_time = end_time - start_time
    minutes = elapsed_time // 60
    num_chars = len(text)
    num_words = len(text.split())

    chars_per_minute = num_chars / elapsed_time * 60 # Calculate characters per minute
    words_per_minute = num_words / elapsed_time * 60 # Calculate words per minute

    return chars_per_minute, words_per_minute


def typing_test():
    text = "This is a typing test. It measures your typing speed and accuracy. Type the following text as quickly and accurately as possible."
    print("Enter the following text:")
    print(text)

    input("Press Enter to start...")

    start_time = time.time() # Get the current time
    user_input = input("Start typing: ")
    end_time = time.time() # Get the current time

    chars_per_minute, words_per_minute = calculate_speed(start_time, end_time, text) # Calculate typing speed
    accuracy = calculate_accuracy(user_input, text) # Calculate accuracy

    print("Results:")
    print(f"Typing Speed: {chars_per_minute:.2f} characters per minute")
    print(f"Typing Speed: {words_per_minute:.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_test()