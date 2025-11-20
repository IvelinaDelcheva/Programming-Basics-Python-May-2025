from math import floor

number_of_tournaments = int(input())
initial_points = int(input())

tournament_points = 0
won_tournaments = 0


for _ in range(number_of_tournaments):
    tournament_stage = input()

    if tournament_stage == 'W':
        tournament_points += 2000 
        won_tournaments += 1
    elif tournament_stage == 'F':
        tournament_points += 1200  
    elif tournament_stage == 'SF':
        tournament_points += 720 

final_points = tournament_points + initial_points
average_points = floor(tournament_points / number_of_tournaments)
won_tournaments_percent = (won_tournaments / number_of_tournaments) * 100

print(f'Final points: {final_points}')
print(f'Average points: {average_points}')
print(f'{won_tournaments_percent:.2f}%')

