# Your program should have two classes – Books and GoldenEditionBooks.
# Book - represents a book that holds title, author and price. 
# A book should offer information about itself in the format shown in the output below.
# GoldenEditionBook - represents a special book that holds the same properties 
# as any Book, but its price is always 30% higher.

class Book:
    def __init__(self, author, title, price):
        self.author = author
        self.title = title
        self.price = price
    
    def __str__(self):
        return f"Type: {Book.__name__}\nTitle: {self.title}\nAuthor: {self.author}\nPrice: {self.price:.2f}"
        

    @property
    def author(self):
        return self.__author
    
    # Setter checks if the name of the author has digits in it
    @author.setter
    def author(self, value):
        for letter in value:
            if letter.isdigit():
                raise Exception("Author not valid!")
        self.__author = value
    

    @property
    def title(self):
        return self.__title
    
    # If the title is shorten than 3 characters raise exception
    @title.setter
    def title(self, value):
        if len(value) < 3:
            raise Exception("Title not valid!")
        self.__title = value
    

    @property
    def price(self):
        return self.__price
    
    #Setter checks if the price is an invalid number (negative or 0)
    @price.setter
    def price(self, value):
        if value == 0 or value < 0:
            raise Exception("Price not valid!")
        self.__price = value


class GoldenEditionBook(Book):
    def __init__(self, author, title, price):
        super().__init__(author, title, price)
        self.price += price * 0.30
    
    def __str__(self):
        return f"Type: {GoldenEditionBook.__name__}\nTitle: {self.title}\nAuthor: {self.author}\nPrice: {self.price:.2f}"

author = input()
title = input()
price = float(input())

try:
    book = Book(author, title, price)
    golden_book = GoldenEditionBook(author, title, price)
    print(book)
    print()
    print(golden_book)
except Exception as f:
    print(f)