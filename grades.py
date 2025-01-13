def main():
    grades = {"Maya": 100, "JP": 99, "Erica": 98, "Vincent": 80}
    fetch_grade(grades)

def fetch_grade(student_grades):
    for grade in student_grades: 
        print(f"{grade} has a grade of {student_grades[grade]}")


main()