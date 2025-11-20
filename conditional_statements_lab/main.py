# we can multiply string but we cannot contacatenate str with int
print('ab' * 10)

#  the wprd pass is used so the program does not underlined in red
color = 'red'

if color == 'red':
    pass
else:
    pass

# rounds functions it round it towards even numbers, rounds .5 to even
# rounds it to the second decimal place
print(round(123.456, 2))

# formatting f string to choose how many decimal places we want
print(f'{123.456:.2f}')


number = 123.456
# formatting f string to choose how many decimal places we want
print(f'{number:.2f}')

# when we have only if constructions they are always checked
age = int(input())

if age == 1:
    pass

if age == 2:
    pass


if age == 1:
    pass
elif age == 2:
    pass
elif age == 3:
    pass

# variable life 
# if if condition is met the local variable will be printed

current_day = 'Monday'

if current_day == 'Monday':
    salary = 1000
print(salary)

# else it will give an error
current_day = 'Monday'

if current_day == 'Friday':
    # salary = 1000
    pass
print(salary)

# thus 
salary = 0

current_day = 'Monday'

if current_day == 'Friday':
    # salary = 1000
    pass
print(salary)
