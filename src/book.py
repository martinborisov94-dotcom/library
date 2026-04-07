
""" Module for the Book class. """


class Book:
    """ A class representing a book in a library system.

    This class encapsulates the properties of a book including its title, author,
    category, and availability status. All attributes are private to ensure
    encapsulation. """


    def __init__(self, title: str, author: str, category: str):
        self.__title = title
        self.__author = author
        self.__category = category
        self.__is_available = True
        print(f"Book created: {self.__title} by {self.__author} \
               in category {self.__category} created.")

    def __eq__(self, other) -> bool:
        if isinstance(other, Book):
            return self.__title == other.get_title() and \
                   self.__author == other.get_author() and \
                   self.__category == other.get_category()
        return False

    def get_title(self) -> str:
        """ Returns the title of the book. """
        return self.__title

    def get_author(self) -> str:
        """ Returns the author of the book. """
        return self.__author

    def get_category(self) -> str:
        """ Returns the category of the book. """
        return self.__category

    def is_available(self) -> bool:
        """ Returns True if the book is available for borrowing, False otherwise. """
        return self.__is_available

    def borrow_book(self) -> bool:
        """ Marks the book as borrowed if it is available. """
        if self.is_available():
            self.__is_available = False
            return True
        return False

    def return_book(self) -> None:
        """ Marks the book as returned and available for borrowing. """
        self.__is_available = True
