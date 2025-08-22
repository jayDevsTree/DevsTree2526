class Book:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.available = True

    def display_info(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'ISBN: {self.isbn}')
        print(f'Year: {self.year}')
        print(f'Available: {"Yes" if self.available else "No"}')


class Library:
    def __init__(self):
        self.catalog = {}

    def input_book_details(self):
        title = input("Enter Book Title: ")
        author = input("Enter Author: ")
        isbn = input("Enter ISBN: ")

        while True:
            try:
                year = int(input("Enter Year: "))
                if 1500 <= year <= 2025:
                    break
                else:
                    print("Enter year between 1500 and 2025")
            except ValueError:
                print("Invalid Year! Enter Valid Year.")

        return Book(title, author, isbn, year)

    def add_book(self):
        book = self.input_book_details()
        if book.isbn not in self.catalog:
            self.catalog[book.isbn] = book
            print(f'Book "{book.title}" added successfully.')
        else:
            print("Book with this ISBN already exists.")

    def display_all_books(self):
        if not self.catalog:
            print("Library catalog is empty.")
        else:
            print("\n--- Library Catalog ---")
            for book in self.catalog.values():
                book.display_info()
                print()

    def borrow_book(self):
        isbn = input("Enter ISBN of the book to borrow: ")
        book = self.catalog.get(isbn)
        if book:
            if book.available:
                book.available = False
                print(f'You borrowed "{book.title}".')
            else:
                print("Book is already borrowed.")
        else:
            print("Book not found.")

    def return_book(self):
        isbn = input("Enter ISBN of the book to return: ")
        book = self.catalog.get(isbn)
        if book:
            if not book.available:
                book.available = True
                print(f'You returned "{book.title}".')
            else:
                print("Book was not borrowed.")
        else:
            print("Book not found.")

    def search_book(self):
        title = input("Enter book title to search: ").lower()
        found = False
        for book in self.catalog.values():
            if book.title.lower() == title:
                print("Book Found:")
                book.display_info()
                found = True
                break
        if not found:
            print("Book not found.")


def Controlcode():
    lib = Library()
    while True:
        print('\n----- Library Management System -----')
        print('''
        1 --> Add Book
        2 --> Display All Books
        3 --> Borrow Book
        4 --> Return Book
        5 --> Search Book
        (press anything else to Exit)''')

        user_choice = input("Enter Choice: ")

        try:
            user_choice = int(user_choice)
        except ValueError:
            print("Thank You!")
            break

        if user_choice == 1:
            lib.add_book()
        elif user_choice == 2:
            lib.display_all_books()
        elif user_choice == 3:
            lib.borrow_book()
        elif user_choice == 4:
            lib.return_book()
        elif user_choice == 5:
            lib.search_book()
        else:
            print("Thank You!")
            break


if __name__ == '__main__':
    Controlcode()
