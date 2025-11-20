student_name = input()

grades_total = 0
years_counter = 0
failed_years = 0

while years_counter < 12:
    annual_grade = float(input())
    
    if annual_grade < 4:
        failed_years += 1
        if failed_years > 1:
            failed_years = years_counter + 1
            print(f'{student_name} has been excluded at {years_counter} grade')
            break
        continue
    years_counter += 1
    grades_total += annual_grade
else:
    average_grade = grades_total / 12
    print(f'{student_name} graduated. Average grade: {(average_grade / 12):.2f}')
