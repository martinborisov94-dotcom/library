
""" Module for the Library class. """

from src.book import Book
from src.user import User

class Library:
    """ A class representing library management.

    This class encapsulates the properties of a library including all users and books.
    All attributes are private to ensure encapsulation. """

    def __init__(self):
        self.__all_books: list[Book] = []
        self.__all_users: list[User] = []

    def add_book(self, new_book: Book) -> None:
        "Add new book to the library"
        if not new_book in self.__all_books:
            self.__all_books.append(new_book)
            print(f"New book is addded {new_book.get_title}")
        else:
            print(f"Book {new_book.get_title} already exists")

    def register_user(self, new_user: User) -> str:
        "Add new users"
        if not new_user in self.__all_users:
            self.__all_users.append(new_user)
            print(f"New user is addded {new_user.get_name}")
        else:
            print(f"Book {new_user.get_name} already exists")

    def get_available_books(self) -> list:
        "Return all available books in th library"
        available_books = []
        for book in self.__all_books:
            if book.is_available:
                available_books.append(book)
        print(f"Available books are: {available_books}")
        return available_books

    def get_all_users(self) -> int:
        "Returns all users"
        return self.__all_users

    def get_all_books(self) -> list:
        "Returns all books"
        return self.__all_books
