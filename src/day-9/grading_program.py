student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {
    "Outstanding": range(91, 101),
    "Exceeds Expectations": range(80, 91),
    "Acceptable": range(71, 81),
    "Fail": range(71),
}

for score in student_scores:
    for grade in student_grades:
        if student_scores[score] in student_grades[grade]:
            print(f"{score} - {grade}")
            break
