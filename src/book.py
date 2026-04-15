
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
        """Return the title of this book.

        Returns:
            str: The book title as a non-empty string.
        """
        return self._title

    def get_author(self) -> str:
        """Return the author of this book.

        Returns:
            str: The author of the book as a non-empty string.
        """
        return self._author

    def get_category(self) -> str:
        """Return the category of this book.

        Returns:
            str: The category of the book as a non-empty string.
        """
        return self._category

    def is_available(self) -> bool:
        """Return True if the book is available for borrowing, False otherwise.

        Returns:
            bool: True if the book is available, False otherwise.
        """
        return self._is_available

    def borrow_book(self) -> None:
        """Marks the book as borrowed if it is available.

        This method sets the book's availability status to False if it is currently available.
        """
        if self.is_available():
            self._is_available = False

    def return_book(self) -> None:
        """Marks the book as returned and available for borrowing.

        This method sets the book's availability status to True, indicating
        that it is available for borrowing.
        """
        self._is_available = True
