"""
Module for the User class.
This module provides the User class which represents a user in a library management system.
"""
from src.book import Book


class User:
    """ A class representing a user in a library system. """


    def __init__(self, name: str):
        self._name = name
        self._borrowed_books = []
        self._borrowed_books_limit = 0

    def __eq__(self, other) -> bool:
        return self._name == other.get_name()

    def get_name(self) -> str:
        """Return the name of the user.

        Returns:
            str: The name of the user as a string.
        """
        return self._name

    def get_borrowed_books(self) -> list:
        """Return a list of books currently borrowed by the user.

        Returns:
            list: A list of books currently borrowed by the user.
        """
        return self._borrowed_books

    def add_borrowed_book(self, book_to_borrow: Book) -> None:
        """Add a book to the list of borrowed books if it is available.

        Args:
            book_to_borrow (Book): The book to borrow.

        Returns:
            None
        """
        if book_to_borrow.is_available():
            self._borrowed_books.append(book_to_borrow)
            book_to_borrow.borrow_book()

    def remove_borrowed_book(self, book_to_return: Book) -> None:
        """Remove a book from the list of borrowed books and mark it as returned.

        Args:
            book_to_return (Book): The book to return.

        Returns:
            None
        """
        if book_to_return in self._borrowed_books:
            self._borrowed_books.remove(book_to_return)
            book_to_return.return_book()

    def set_borrowed_books_limit(self, limit: int) -> None:
        """Set the limit for the number of books a user can borrow.

        Args:
            limit (int): The maximum number of books the user can borrow.

        Returns:
            None
        """
        self._borrowed_books_limit = limit
