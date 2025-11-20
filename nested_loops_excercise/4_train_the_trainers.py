jury_number = int(input())
average_final_assesment = 0.0
score_counter = 0

while True:
    presentation = input()
    average_presentation_score = 0.0
    if presentation == 'Finish':
        break

    for _ in range(jury_number):
        jury_score = float(input())
        average_presentation_score += jury_score
        average_final_assesment += jury_score
        score_counter += 1
    
    print(f'{presentation} - {(average_presentation_score / jury_number):.2f}.')

print(f'Student\'s final assessment is {(average_final_assesment / score_counter):.2f}.')
