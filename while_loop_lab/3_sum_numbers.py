number = int(input())
sum = 0

while True:
    input_number = int(input())
    sum += input_number
    
    if sum >= number:
        break
print(sum)


