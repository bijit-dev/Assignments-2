# book_manager.py
from book import Book
from shared_data import books
import file_manager as fm

def add_book():
    title = input("Enter title: ")
    authors = input("Enter authors (comma separated): ").split(",")
    isbn = input("Enter ISBN: ")
    year = input("Enter publishing year: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    
    new_book = Book(title, authors, isbn, year, price, quantity)
    books.append(new_book)
    fm.backup_books()
    print("Book added successfully.")

def view_all_books():
    if books:
        for book in books:
            print(book)
    else:
        print("No books available.")

def search_books():
    search_term = input("Enter title or ISBN to search: ").lower()
    found_books = [book for book in books if search_term in book.title.lower() or search_term in book.isbn]
    if found_books:
        for book in found_books:
            print(book)
    else:
        print("No books found.")

def search_books_by_author():
    search_term = input("Enter author to search: ").lower()
    found_books = [book for book in books if any(search_term in author.lower() for author in book.authors)]
    if found_books:
        for book in found_books:
            print(book)
    else:
        print("No books found.")

def remove_book():
    search_term = input("Enter title or ISBN to remove: ").lower()
    found_books = [book for book in books if search_term in book.title.lower() or search_term in book.isbn]
    if found_books:
        for index, book in enumerate(found_books):
            print(f"{index + 1}. {book}")
        choice = int(input("Enter the number of the book to remove: "))
        books.remove(found_books[choice - 1])
        fm.backup_books()
        print("Book removed successfully.")
    else:
        print("No books found.")

def lend_book():
    search_term = input("Enter title or ISBN to lend: ").lower()
    found_books = [book for book in books if search_term in book.title.lower() or search_term in book.isbn]
    if found_books:
        for index, book in enumerate(found_books):
            print(f"{index + 1}. {book}")
        choice = int(input("Enter the number of the book to lend: "))
        selected_book = found_books[choice - 1]
        if selected_book.quantity > 0:
            lend_to = input("Enter the name of the person: ")
            selected_book.quantity -= 1
            selected_book.lent_to = lend_to
            fm.backup_books()
            print("Book lent successfully.")
        else:
            print("Not enough books available to lend.")
    else:
        print("No books found.")

def view_lent_books():
    lent_books = [book for book in books if book.lent_to is not None]
    if lent_books:
        for book in lent_books:
            print(f"{book} lent to {book.lent_to}")
    else:
        print("No books are currently lent.")

def return_book():
    search_term = input("Enter title or ISBN to return: ").lower()
    found_books = [book for book in books if search_term in book.title.lower() or search_term in book.isbn]
    if found_books:
        for index, book in enumerate(found_books):
            if book.lent_to is not None:
                print(f"{index + 1}. {book}")
        choice = int(input("Enter the number of the book to return: "))
        selected_book = found_books[choice - 1]
        selected_book.quantity += 1
        selected_book.lent_to = None
        fm.backup_books()
        print("Book returned successfully.")
    else:
        print("No books found.")
