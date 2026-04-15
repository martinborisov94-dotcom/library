
""" Module for the User class. """
from src.book import Book


class User:
    """ A class representing a user in a library system. """


    def __init__(self, name: str):
        self._name = name
        self._borrowed_books = []
        self._borrowed_books_limit = -1 # -1 is default value for unlimited books

    def __eq__(self, other) -> bool:
        return self._name == other.get_name()

    def get_name(self) -> str:
        """ Returns the name of the user. """
        return self._name

    def get_borrowed_books(self) -> list:
        """ Returns a list of books currently borrowed by the user. """
        return self._borrowed_books

    def add_borrowed_book(self, book: Book) -> None:
        """ Adds a book to the list of borrowed books. """
        if self._borrowed_books_limit != -1 and \
              len(self._borrowed_books) >= self._borrowed_books_limit:
            print(f"User '{self._name}' has reached the borrowing limit  \
                  of {self._borrowed_books_limit} books.")
            return

        self._borrowed_books.append(book)
        book.borrow_book()

    def remove_borrowed_book(self, book: Book) -> None:
        """ Removes a book from the list of borrowed books. """
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            book.return_book()

    def set_borrowed_books_limit(self, limit: int) -> None:
        """ Sets the limit for the number of books a user can borrow. """
        self._borrowed_books_limit = limit
