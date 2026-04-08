""" Unit tests for Library class."""

from src.library import Library
from src.book import Book
from src.user import User


class TestLibrary():
    """ Unit test for Library class."""

    def test_add_new_book(self):
        """Test for adding a new book to the library """
        library = Library()
        book1 = Book("Book1", "Author1", "Category1")
        library.add_book(book1)
        expected_result = [book1]
        actual_result = library.get_all_books()
        assert actual_result == expected_result

    def test_add_twice_same_book(self):
        """Test for adding the same book twice to the library """
        library = Library()
        book1 = Book("Book1", "Author1", "Category1")
        library.add_book(book1)
        library.add_book(book1)
        expected_result = [book1]
        actual_result = library.get_all_books()
        assert actual_result == expected_result

    def test_empty_books_library(self):
        """Test for empty library """
        library = Library()
        excted_result = []
        actual_result = library.get_all_books()
        assert actual_result == excted_result

    def test_register_user(self):
        """Test for registering a new user to the library """
        library = Library()
        user1 = User("User1")
        library.register_user(user1)
        expected_result = [user1]
        actual_result = library.get_all_users()
        assert actual_result == expected_result

    def test_register_twice_same_user(self):
        """Test for registering the same user twice to the library """
        library = Library()
        user1 = User("User1")
        library.register_user(user1)
        library.register_user(user1)
        expected_result = [user1]
        actual_result = library.get_all_users()
        assert actual_result == expected_result


    def test_all_books_avaible(self):
        """Test for getting all available books in the library """
        library = Library()
        book1 = Book("Book1", "Author1", "Category1")
        book2 = Book("Book2", "Author2", "Category2")
        library.add_book(book1)
        library.add_book(book2)
        expected_result = [book1, book2]
        actual_result = library.get_available_books()
        assert actual_result == expected_result

    def test_no_books_avaible(self):
        """Test for getting all available books in the library when no books are available """
        library = Library()
        book1 = Book("Book1", "Author1", "Category1")
        book2 = Book("Book2", "Author2", "Category2")
        library.add_book(book1)
        library.add_book(book2)
        book1.is_available = False
        book2.is_available = False
        expected_result = []
        actual_result = library.get_available_books()
        assert actual_result == expected_result

    def test_some_books_avaible(self):
        """Test for getting all available books in the library when some books are available """
        library = Library()
        book1 = Book("Book1", "Author1", "Category1")
        book2 = Book("Book2", "Author2", "Category2")
        library.add_book(book1)
        library.add_book(book2)
        book1.is_available = False
        expected_result = [book2]
        actual_result = library.get_available_books()
        assert actual_result == expected_result

    def test_empty_users_library(self):
        """Test for getting all users in the library when no users are registered """
        library = Library()
        expected_result = []
        actual_result = library.get_all_users()
        assert actual_result == expected_result
