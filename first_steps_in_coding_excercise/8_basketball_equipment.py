basketball_tax_per_year = int(input())

basketball_trainers = basketball_tax_per_year * 0.6
basketball_tracksuit = basketball_trainers * 0.8
basketball_bowl = basketball_tracksuit / 4
basketball_accessories = basketball_bowl / 5

total_backetball_expenses_per_year = basketball_trainers + basketball_tracksuit + basketball_bowl + basketball_accessories + basketball_tax_per_year

print(total_backetball_expenses_per_year)
