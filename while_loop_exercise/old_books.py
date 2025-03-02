

finding_book = input()
books = input()
book_counter = 0
while True:
    book_counter += 1
    books = input()

    if books == finding_book:

        print(f'You checked {book_counter} books and found it.')
        break
    elif books == 'No More Books':
        print(f'The book you search is not here!\nYou checked {book_counter} books.')


