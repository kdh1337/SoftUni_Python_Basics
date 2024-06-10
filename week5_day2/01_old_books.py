book = input()
book_count = 0

while book != 'No More Books':
    search_book = input()
    if search_book == book:
        print(f'You checked {book_count} books and found it.')
        break
    elif search_book == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {book_count} books.')
        break
    else:
        book_count += 1