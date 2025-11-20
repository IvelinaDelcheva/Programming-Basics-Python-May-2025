cake_width = int(input())
cake_lenght = int(input())

total_pieces = cake_width * cake_lenght
no_more_cake = False

command = input()
while command != 'STOP':
    pieces_taken = int(command)
    
    total_pieces -= pieces_taken

    if total_pieces <= 0:
        no_more_cake = True
        break

    command = input()

if no_more_cake:
    print(f'No more cake left! You need {abs(total_pieces)} pieces more.')
else:
    print(f'{total_pieces} pieces are left.')