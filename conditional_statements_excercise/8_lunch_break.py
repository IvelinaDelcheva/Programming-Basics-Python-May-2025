# 1.	Име на сериал – текст
# 2.	Продължителност на епизод  – цяло число в диапазона [10… 90]
# 3.	Продължителност на почивката  – цяло число в диапазона [10… 120]
from math import ceil 

series_name = input()
series_time_lenght = int(input())
lunch_break_time_lenght = int(input())

time_lenght_for_lunch = lunch_break_time_lenght / 8
leisure_time_lenght = lunch_break_time_lenght / 4

left_movie_time = lunch_break_time_lenght - time_lenght_for_lunch - leisure_time_lenght

diff = ceil(abs(series_time_lenght - left_movie_time))

if left_movie_time >= series_time_lenght:
    print(f'You have enough time to watch {series_name} and left with {diff} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {series_name}, you need {diff} more minutes.')



