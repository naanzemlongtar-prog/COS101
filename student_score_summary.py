# student_score_summary.py

num_students = int(input("Enter the number of students: "))

while num_students <= 0:
    print("Invalid number of students. Try again.")
    num_students = int(input("Enter the number of students: "))

total_score = 0
passes = 0
failures = 0

for student in range(1, num_students + 1):
    score = float(input(f"Enter score for student {student}: "))

    while score < 0 or score > 100:
        print("Invalid score. Score must be between 0 and 100.")
        score = float(input(f"Enter score for student {student} again: "))

    total_score += score

    if score >= 50:
        passes += 1
    else:
        failures += 1

average_score = total_score / num_students

print("STUDENT SCORE SUMMARY ")
print(f"Number of students: {num_students}")
print(f"Total score: {total_score}")
print(f"Average score: {round(average_score, 2)}")
print(f"Number of passes: {passes}")
print(f"Number of failures: {failures}")
