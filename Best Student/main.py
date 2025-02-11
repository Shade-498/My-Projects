students = [
    {"name": "John", "surname": "Doe", "grades": [5, 5, 4, 4]},
    {"name": "Jane", "surname": "Doe", "grades": [4, 3, 4, 3, 5]},
    {"name": "Bill", "surname": "Gates", "grades": [5, 5, 5, 3]},
    {"name": "Steve", "surname": "Jobs", "grades": [3, 5, 4, 3, 3, 5]},
    {"name": "Guido", "surname": "Van Rossum", "grades": [5, 3, 5, 4, 5, 5, 3, 5]},
    {"name": "Elon", "surname": "Musk", "grades": None}
]

def get_best_students(*, students: list[dict]) -> list[dict]:
    list_of_best_students = []
    needed_grade = 4.5
    # Loop
    for student in students:
    # Set needed grade
      grades = student['grades']
    # If grade equal None
      if grades == None:
        grades = [0]
    # Calculate average grade
      average_grade = sum(grades) / len(grades)
    # Check if average grade is more than needed grade
      if average_grade >= needed_grade:
        list_of_best_students.append(student)
    # Return list of best students
    return list_of_best_students

# Call function
print((get_best_students(students=students)))