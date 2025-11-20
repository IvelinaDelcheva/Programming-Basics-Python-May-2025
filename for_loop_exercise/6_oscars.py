actor_name = input()
academy_points = float(input())
number_of_jury = int(input())

is_nominated = False

for _ in range(number_of_jury):
    jury_name = input()
    jury_points = float(input())

    academy_points += (len(jury_name) * jury_points / 2)

    if academy_points >= 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {(academy_points):.1f}!')
        is_nominated = True
        break

if not is_nominated:
    print(f'Sorry, {actor_name} you need {(1250.5 - academy_points):.1f} more!')