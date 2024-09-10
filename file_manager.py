# file_manager.py
import json
from shared_data import books
from book import Book

FILE_PATH = "books.json"

def backup_books():
    with open(FILE_PATH, "w") as file:
        json_books = [book.__dict__ for book in books]
        json.dump(json_books, file)

def restore_books():
    try:
        with open(FILE_PATH, "r") as file:
            json_books = json.load(file)
            for book_data in json_books:
                book = Book(**book_data)
                books.append(book)
    except FileNotFoundError:
        pass
