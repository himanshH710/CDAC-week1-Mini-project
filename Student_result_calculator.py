print("=" * 50)
print("      STUDENT RESULT CALCULATOR")
print("=" * 50)

# Student Name
student_name = input("Enter Student Name: ")

# Empty list for marks
marks = []

# Taking marks of 5 subjects
for i in range(1, 6):
    mark = int(input(f"Enter marks for Subject {i}: "))
    marks.append(mark)

# Calculations
total = 0

for mark in marks:
    total = total + mark

average = total / len(marks)
percentage = (total / 500) * 100

highest = marks[0]
lowest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

# Count subjects above 90
above_90 = 0

for mark in marks:
    if mark >= 90:
        above_90 += 1

# Pass or Fail
result = "PASS"

for mark in marks:
    if mark < 33:
        result = "FAIL"
        break

# Grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Output
print("\n" + "=" * 50)
print("STUDENT RESULT")
print("=" * 50)

print("Student Name      :", student_name)
print("Marks             :", marks)
print("Total Marks       :", total)
print("Average Marks     :", round(average, 2))
print("Percentage        :", round(percentage, 2), "%")
print("Highest Marks     :", highest)
print("Lowest Marks      :", lowest)
print("Subjects >= 90    :", above_90)
print("Grade             :", grade)
print("Result            :", result)

print("=" * 50)