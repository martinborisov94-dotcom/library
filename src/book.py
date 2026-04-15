
"""
Module for the Book class.
This module provides the Book class which represents a book in a library management system.
"""


class Book:
    """ A class representing a book in a library system.

    This class encapsulates the properties of a book including its title, author,
    category, and availability status. All attributes are private to ensure
    encapsulation. """


    def __init__(self, title: str, author: str, category: str):
        self._title = title
        self._author = author
        self._category = category
        self._is_available = True


    def __eq__(self, other) -> bool:
        return self._title == other.get_title() and \
                self._author == other.get_author() and \
                self._category == other.get_category()


    def get_title(self) -> str:
        """ Returns the title of the book. """
        return self._title

    def get_author(self) -> str:
        """ Returns the author of the book. """
        return self._author

    def get_category(self) -> str:
        """ Returns the category of the book. """
        return self._category

    def is_available(self) -> bool:
        """ Returns True if the book is available for borrowing, False otherwise. """
        return self._is_available

    def borrow_book(self) -> None:
        """ Marks the book as borrowed if it is available. """
        if self.is_available():
            self._is_available = False

    def return_book(self) -> None:
        """ Marks the book as returned and available for borrowing. """
        self._is_available = True
