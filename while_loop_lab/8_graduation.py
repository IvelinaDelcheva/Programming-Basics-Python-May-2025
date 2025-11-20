# student_name = input()

# counter = 0
# sum = 0
# low_grades = 0

# while counter != 12:
#     current_grade = float(input())

#     if current_grade < 4:
#         low_grades += 1
#         if low_grades > 1:
#             break
    
#     sum += current_grade
#     counter += 1

# if counter == 12:
#     print(f'{student_name} graduated. Average grade: {(sum / 12):.2f}')
# else:
#     print(f'{student_name} has been excluded at {counter} grade')

student_name = input()

average_grade = 0.0
grade_counter = 0
times_failed = 0
grade = 1
failed = False
while grade <= 12:
    grade_score = float(input())
    

    if grade_score >= 4:
        average_grade += grade_score
    else:
        times_failed += 1
        if times_failed > 1:
            print(f'{student_name} has been excluded at {grade_counter} grade')
            failed = True
            break
    grade_counter += 1
    grade += 1

if not failed:
    print(f'{student_name} graduated. Average grade: {(average_grade / 12):.2f}')


