
student_name = input("Enter student's name: ")

coursework_score = float(input("Enter coursework score (out of 30): "))

examination_score = float(input("Enter examination score (out of 70): "))

if coursework_score < 0 or coursework_score > 30:
    print("Error: Coursework score must be between o and 30.")

elif examination_score < 0 or examination_score > 70:
    print("Error: Examination score must be between 0 and 70.")

else:
    total_score = coursework_score + examination_score

    if total_score >= 70:
        grade = "A"
    elif total_score >= 60:
        grade = "B"
    elif total_score >= 50:
        grade = "C"
    elif total_score >= 45:
        grade = "D"
    elif total_score >= 40:
        grade = "E"
    else:
        grade = "F"

    if total_score >= 50:
        progression = "Pass"
    else:
        progression = "Resit required"

    print()
    print("STUDENT RESULT SUMMARY")
    print(f"Coursework Score: {coursework_score}/30")
    print(f"Examination Score: {examination_score}/70")
    print(f"Total Score: {total_score}/100")
    print("Grade: {grade}")
    print("Progression Decision: {progression}")
