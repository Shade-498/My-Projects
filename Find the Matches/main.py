import re

# Find the matches
text = input("Enter text: ")
pattern = input("Enter pattern: ")

matches = re.findall(pattern, text)

print("Matches:", len(matches))