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
        """ Returns the name of the user. """
        return self._name

    def get_borrowed_books(self) -> list:
        """ Returns a list of books currently borrowed by the user. """
        return self._borrowed_books

    def add_borrowed_book(self, book_to_borrow: Book) -> None:
        """ Adds a book to the list of borrowed books. """
        if book_to_borrow.is_available():
            self._borrowed_books.append(book_to_borrow)
            book_to_borrow.borrow_book()

    def remove_borrowed_book(self, book_to_return: Book) -> None:
        """ Removes a book from the list of borrowed books. """
        if book_to_return in self._borrowed_books:
            self._borrowed_books.remove(book_to_return)
            book_to_return.return_book()

    def set_borrowed_books_limit(self, limit: int) -> None:
        """ Sets the limit for the number of books a user can borrow. """
        self._borrowed_books_limit = limit
