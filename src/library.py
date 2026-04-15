
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

    def register_user(self, new_user: User) -> str:
        "Add new users"
        if not new_user in self.__all_users:
            self.__all_users.append(new_user)


    def get_available_books(self) -> list:
        "Return all available books in th library"
        available_books = []
        for book in self.__all_books:
            if book.is_available:
                available_books.append(book)
        return available_books

    def get_all_users(self) -> list:
        "Returns all users"
        return self.__all_users

    def get_all_books(self) -> list:
        "Returns all books"
        return self.__all_books

    def all_books_and_users(self) -> None:
        "Track all users and books"
        print(f"All users: {self.__all_users}")
        print(f"All books: {self.__all_books}")

    def find_book_by_author(self, author: str) -> Book:
        """Search book by author name"""
        for book in self.__all_books:
            if book.get_author() == author:
                return book
        print(f"No book found by author {author}")
        return None

    def find_book_by_category(self, category: str) -> Book:
        """Search book by category name"""
        for book in self.__all_books:
            if book.get_category() == category:
                return book
        return None
