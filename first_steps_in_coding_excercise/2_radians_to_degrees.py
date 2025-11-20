# import math 

# import only what we need from the library
from math import pi

radians = float(input())

# alternative for pi but not complete after the decimal so it gives wrong answer
# result = (radians * 180) / 3.14

result = (radians * 180) / pi

print(result)