target_steps = 10000

total_steps = 0
goal_reached = False

command = input()
while command != 'Going home':
    daily_steps = int(command)

    total_steps += daily_steps
    if total_steps >= target_steps:
        goal_reached = True
        break

    command = input()

if command == 'Going home':
    steps_to_home = int(input())
    total_steps += steps_to_home
    if total_steps >= target_steps:
        goal_reached = True

diff = abs(target_steps - total_steps)

if not goal_reached:
    print(f'{diff} more steps to reach goal.')
else:
    print(f'Goal reached! Good job!')
    print(f'{diff} steps over the goal!')

