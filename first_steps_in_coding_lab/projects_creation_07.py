architect_name = input()
number_of_projects = int(input())

needed_hours = number_of_projects * 3

# moving to next line f is used for formatting the text again
print(f'The architect {architect_name} will need {needed_hours} '
      f'hours to complete {number_of_projects} project/s.')