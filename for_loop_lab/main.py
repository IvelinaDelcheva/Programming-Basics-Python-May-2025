# for loop 

# 1 is the starting index as usually starts form 0
# 11 is the end of rang but -1 so it will print up to 10
# 2 is step 2. It  will prine 1, 3, 5 etc. It can be step 1 or any
# for i in range(1, 11, 2):
#     print(i)

# for i in range(11):
#     print(i)

# step can be negative as well
# for i in range(11, 0, -2):
#     print(i)

# if we do not wan to use the index we use _
# in that way we only use the iterations
# for _ in range(5):
#     number = int(input())
#     print(number)

for i in range(1, 10 + 1):
    print(i)

import sys

#  this is used to find minimal and maximum numbers
max_number = -sys.maxsize
min_number = sys.maxsize

# \n goes to the next line