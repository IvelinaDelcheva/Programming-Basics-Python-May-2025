looking_for_book = input()

book_counter = 0
book_found = False

book_input = input()
while book_input != 'No More Books':

    if book_input == looking_for_book:
        book_found = True
        break
    
    book_counter += 1
    book_input = input()

if book_found:
    print(f'You checked {book_counter} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {book_counter} books.')