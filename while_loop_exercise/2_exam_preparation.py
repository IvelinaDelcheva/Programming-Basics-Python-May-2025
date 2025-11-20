number_of_bad_scores = int(input())

bas_score_counter = 0
number_of_problems = 0
average_score = 0
need_break = False

command = input()
while command != 'Enough':
    problem_name = command
    problem_score = int(input())

    if problem_score <= 4:
        bas_score_counter += 1
        if bas_score_counter == number_of_bad_scores:
            need_break = True
            break
    
    number_of_problems += 1
    average_score += problem_score

    command = input()

final_score = average_score / number_of_problems

if need_break:
    print(f'You need a break, {bas_score_counter} poor grades.')
else:
    print(f'Average score: {final_score:.2f}')
    print(f'Number of problems: {number_of_problems}')
    print(f'Last problem: {problem_name}')