from collections import Counter

def analyze_text(text):
    # Convert text to lowercase and split into words
    words = text.lower().split()

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Find the most common and least common word
    most_common_word, most_common_count = word_counts.most_common(1)[0]
    least_common_word, least_common_count = word_counts.most_common()[-1]

    # Print the results
    print("Count of each word:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

    print(f"\nMost common word: '{most_common_word}' (appears {most_common_count} times)")
    print(f"Least common word: '{least_common_word}' (appears {least_common_count} times)")

# Example usage
if __name__ == "__main__":
  text = input("Enter a text to analyze: ")
  analyze_text(text)