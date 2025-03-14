def quiz_game():
    questions = [
        {
            "question": "Which programming language is considered the most popular in 2024?",
            "options": ["Python", "Java", "C++", "JavaScript"],
            "answer": "Python"
        },
        {
            "question": "Which data type in Python is used to store integers?",
            "options": ["int", "float", "str", "bool"],
            "answer": "int"
        },
        {
            "question": "Which operator is used for exponentiation in Python?",
            "options": ["^", "**", "*", "//"],
            "answer": "**"
        },
        {
            "question": "Which method is used to add an element to the end of a list in Python?",
            "options": ["append()", "insert()", "add()", "push()"],
            "answer": "append()"
        },
        {
            "question": "Which symbol is used for single-line comments in Python?",
            "options": ["//", "#", "--", "/*"],
            "answer": "#"
        },
        {
            "question": "Which module in Python is used for working with regular expressions?",
            "options": ["re", "regex", "regexp", "pyregex"],
            "answer": "re"
        },
        {
            "question": "Which data type in Python is immutable?",
            "options": ["list", "dict", "tuple", "set"],
            "answer": "tuple"
        },
        {
            "question": "Which method is used to remove an item from a dictionary by key in Python?",
            "options": ["remove()", "delete()", "pop()", "clear()"],
            "answer": "pop()"
        },
        {
            "question": "Which operator is used to check for equality in Python?",
            "options": ["=", "==", "===", "!="],
            "answer": "=="
        },
        {
            "question": "Which module in Python is used for mathematical functions?",
            "options": ["math", "calc", "numpy", "random"],
            "answer": "math"
        }
    ]

    score = 0

    print("Welcome to the Python Quiz!")
    print("Answer the following questions:")

    for i, q in enumerate(questions, 1):
        print('=' * 30) # Print separator
        print(f"Question {i}: {q['question']}") # Print question
        for j, option in enumerate(q['options'], 1	):
            print(f"{j}. {option}") # Print options

        user_answer = input("Your answer (enter the option number): ")

        if q['options'][int(user_answer) - 1] == q['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", q['answer'])

    print('=' * 30) # Print separator
    print(f"Quiz completed! Your score: {score}/{len(questions)}")


if __name__ == "__main__":
    quiz_game()