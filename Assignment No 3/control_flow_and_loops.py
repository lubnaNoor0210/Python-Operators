# CONTROL FLOW
# Control flow refers to the order in which statements are executed in a program.
# In Python, decision-making is achieved using if, elif, and else statements,along with comparison and logical operators.
# LOOPS are used to repeat a block of code multiple times

# Grading System:
def get_grade(score):
    if score >= 90:
        grade = 'A+'
    elif score >= 80:
        grade = 'A'
    elif score >= 70:
        grade = 'B'
    elif score >= 60:
        grade = 'C'
    elif score >= 50:
        grade = 'D'
    else:
        grade = 'F'
    return grade

num_students = int(input("Enter number of students: "))

for i in range(num_students):
    score = float(input(f"Enter score for student {i + 1}: "))
    grade = get_grade(score)
    print(f"Student {i + 1} got grade: {grade}")

    
