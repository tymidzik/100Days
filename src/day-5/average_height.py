student_heights = input("Input a list of students heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

sum = 0
lenght = 0
for student_height in student_heights:
    sum += student_height
    lenght = lenght + 1

result = round(sum / lenght)
print(result)
