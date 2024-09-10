# book.py
class Book:
    def __init__(self, title, authors, isbn, year, price, quantity, lent_to=None):
        self.title = title
        self.authors = authors
        self.isbn = isbn
        self.year = year
        self.price = price
        self.quantity = quantity
        self.lent_to = lent_to

    def __str__(self):
        authors = ', '.join(self.authors)
        return f"Title: {self.title}, Authors: {authors}, ISBN: {self.isbn}, Year: {self.year}, Price: {self.price}, Quantity: {self.quantity}, Lent to: {self.lent_to}"
