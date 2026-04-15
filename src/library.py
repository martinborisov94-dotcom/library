"""
Module for the Library class.
This module provides the Library class which represents a library in a library management system.
"""

from src.book import Book
from src.user import User

class Library:
    """ A class representing library management.

    This class encapsulates the properties of a library including all users and books.
    All attributes are private to ensure encapsulation. """

    def __init__(self):
        self._all_books: list[Book] = []
        self._all_users: list[User] = []

    def add_book(self, new_book: Book) -> None:
        """Add a new book to the library if it is not already present.

        Args:
            new_book (Book): The book to add to the library collection.

        Returns:
            None
        """
        if not new_book in self._all_books:
            self._all_books.append(new_book)

    def register_user(self, new_user: User) -> str:
        """Add a new user to the library if they are not already registered.

        Args:
            new_user (User): The user to register in the library.

        Returns:
            None
        """
        if not new_user in self._all_users:
            self._all_users.append(new_user)


    def get_available_books(self) -> list:
        """Return all available books in the library.

        Returns:
            list: A list of available books.
        """
        available_books = []
        for book in self._all_books:
            if book.is_available:
                available_books.append(book)
        return available_books

    def get_all_users(self) -> list:
        """Return all registered users.

        Returns:
            list: A list containing all users.
        """
        return self._all_users

    def get_all_books(self) -> list:
        """Return all books in the library.

        Returns:
            list: A list containing all books.
        """
        return self._all_books

    def all_books_and_users(self) -> None:
        """Track all users and books"""
        print(f"All users: {self._all_users}")
        print(f"All books: {self._all_books}")

    def find_book_by_author(self, author: str) -> Book:
        """Search book by author name

        Args:
            author (str): The author name to search for.

        Returns:
            Book: The first book found by the specified author, or None if not found.
        """
        for book in self._all_books:
            if book.get_author() == author:
                return book
        print(f"No book found by author {author}")
        return None

    def find_book_by_category(self, category: str) -> Book:
        """Search book by category name

        Args:
            category (str): The category name to search for.

        Returns:
            Book: The first book found in the specified category, or None if not found.
        """
        for book in self._all_books:
            if book.get_category() == category:
                return book
        return None
