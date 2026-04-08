
""" Module for the User class. """
from src.book import Book


class User:
    """ A class representing a user in a library system. """


    def __init__(self, name: str):
        self.__name = name
        self.__borrowed_books = []
        self.__borrowed_books_limit = -1 # -1 is default value for unlimited books

    def __eq__(self, other) -> bool:
        if isinstance(other, User):
            return self.__name == other.get_name()
        return False

    def get_name(self) -> str:
        """ Returns the name of the user. """
        return self.__name

    def get_borrowed_books(self) -> list:
        """ Returns a list of books currently borrowed by the user. """
        return self.__borrowed_books

    def add_borrowed_book(self, book: Book) -> None:
        """ Adds a book to the list of borrowed books. """
        if self.__borrowed_books_limit != -1 and \
              len(self.__borrowed_books) >= self.__borrowed_books_limit:
            print(f"User '{self.__name}' has reached the borrowing limit  \
                  of {self.__borrowed_books_limit} books.")
            return

        self.__borrowed_books.append(book)
        book.borrow_book()

    def remove_borrowed_book(self, book: Book) -> None:
        """ Removes a book from the list of borrowed books. """
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            book.return_book()
        else:
            print(f"Book '{book.get_title()}' is not in the list of borrowed \
                  books for user '{self.__name}'.")

    def set_borrowed_books_limit(self, limit: int) -> None:
        """ Sets the limit for the number of books a user can borrow. """
        self.__borrowed_books_limit = limit
