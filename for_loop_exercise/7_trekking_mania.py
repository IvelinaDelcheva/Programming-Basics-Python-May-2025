number_of_groups = int(input())

people_Musala = people_Montblan = people_Kilimanjaro = people_K2 = people_Everest = 0

for _ in range(number_of_groups):
    people_in_group = int(input())

    if people_in_group <= 5:
        people_Musala += people_in_group
    elif 6 <= people_in_group <= 12:
        people_Montblan += people_in_group
    elif 13 <= people_in_group <= 25:
        people_Kilimanjaro += people_in_group
    elif 26 <= people_in_group <= 40:
        people_K2 += people_in_group
    elif people_in_group >= 41:
        people_Everest += people_in_group

total_people = people_Musala + people_Montblan + people_Kilimanjaro + people_K2 + people_Everest

print(f'{((people_Musala / total_people) * 100):.2f}%')
print(f'{((people_Montblan / total_people) * 100):.2f}%')
print(f'{((people_Kilimanjaro / total_people) * 100):.2f}%')
print(f'{((people_K2 / total_people) * 100):.2f}%')
print(f'{((people_Everest / total_people) * 100):.2f}%')
