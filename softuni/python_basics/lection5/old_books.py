book_target = input()
bookshelf_total = int(input())
books = None
counter = 0

while counter < bookshelf_total:
    books = input() 
    if books == book_target:
        print(f"You checked {counter} books and found it.")
        break
    counter += 1

if books != book_target:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")
        