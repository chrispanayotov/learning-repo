book_target = input()
bookshelf_total = int(input())

books_checked = 0

while books_checked < bookshelf_total:
    books = input() 
    if books == book_target:
        print(f"You checked {books_checked} books and found it.")
        break
    books_checked += 1
else:
    print("The book you search is not here!")
    print(f"You checked {books_checked} books.")
        