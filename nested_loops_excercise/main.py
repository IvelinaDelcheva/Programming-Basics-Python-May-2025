# enumerate function gives from a string the index and the char
# if we want the index of a digit must be in string first and the parsed to int

num = '10005'
num2 = 10005

for idx, digit in enumerate(str(num)):
    print(idx, digit)

# how to find square root of a number
# ** is to the power of a number
print(5 ** 0.5) 

# or using the math function sqrt
# it will give the same result
from math import sqrt

print(sqrt(5))