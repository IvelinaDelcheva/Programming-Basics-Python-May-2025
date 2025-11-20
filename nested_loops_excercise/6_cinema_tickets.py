total_tickets = 0
student_tickets =  0
standard_tickets =  0
kids_tickets =  0

while True:
    movie_name = input()
    
    if movie_name == 'Finish':
        break
    current_tickets = 0
    free_spaces = int(input())

    for space in range(free_spaces, 0, -1):
        ticket_type = input()

        if ticket_type == 'End':
            break

        total_tickets += 1
        current_tickets += 1

        if ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1 
        elif ticket_type == 'kid':
            kids_tickets += 1 
        
    print(f'{movie_name} - {((current_tickets / free_spaces) * 100):.2f}% full.')

print(f'Total tickets: {total_tickets}')
print(f'{((student_tickets / total_tickets) * 100):.2f}% student tickets.')
print(f'{((standard_tickets / total_tickets) * 100):.2f}% standard tickets.')
print(f'{((kids_tickets / total_tickets) * 100):.2f}% kids tickets.')

