# app.py
import book_manager as bm
import file_manager as fm

def main():
    fm.restore_books()
    menu_text = """
    Library Management System
    1. Add Book
    2. View All Books
    3. Search Book by Title/ISBN
    4. Search Book by Author
    5. View Lent Books
    6. Lend Book
    7. Remove Book
    8. Return Book
    0. Exit
    """
    
    while True:
        print(menu_text)
        choice = input("Enter your choice: ")
        
        if choice == "1":
            bm.add_book()
        elif choice == "2":
            bm.view_all_books()
        elif choice == "3":
            bm.search_books()
        elif choice == "4":
            bm.search_books_by_author()
        elif choice == "5":
            bm.view_lent_books()
        elif choice == "6":
            bm.lend_book()
        elif choice == "7":
            bm.remove_book()
        elif choice == "8":
            bm.return_book()
        elif choice == "0":
            fm.backup_books()
            print("Thanks for using the Library Management System.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
