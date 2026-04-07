
"""Module for unit test for Book class"""

import pytest
from src.book import Book


class TestBook():
    """ Unit test for Book class"""

    def test_title(self):
        """Test if get title works properly"""
        book = Book("IT", "Stephen King", "Horror")
        expected_title = "IT"
        actual_title = book.get_title()
        assert expected_title == actual_title, "Expected book title != actual book title"

    def test_author(self):
        """Test if get author works properly"""
        book = Book("IT", "Stephen King", "Horror")
        expected_author = "Stephen King"
        actual_author = book.get_author()
        assert expected_author == actual_author, "Expected author != actual author"

    def test_category(self):
        """Test if get category works properly"""
        book = Book("IT", "Stephen King", "Horror")
        expected_category = "Horror"
        actual_category = book.get_category()
        assert expected_category == actual_category, "Expected category != actual category"

    def test_availability(self):
        """Test availability"""
        book = Book("IT", "Stephen King", "Horror")
        expected_available = True
        actual_available = book.is_available()
        assert actual_available == expected_available

    def test_two_books_same_attributes(self):
        "Testy two books are the same"
        book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Tragedy")
        book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Tragedy")
        assert book1 == book2, "Books are not the same"

    def test_two_books_different_category(self):
        "Testy two books are not the same"
        book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Tragedy")
        book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Comedy")
        assert book1 != book2, "Books are not the same"

    def test_borrow_when_available_mark_as_unavailable(self):
        """Verify borrowing book after being available and mark as unavaolable"""
        book = Book("Hamlet", "Shakespeare", "Tragedy")
        expected_available = True
        actual_available = book.is_available()
        assert expected_available == actual_available, "Book is not available"

        expected_borrowed = True
        actual_borrow = book.borrow_book()
        assert expected_borrowed == actual_borrow, "Book is borrowed"

        expected_available_after = False
        actual_available_after = book.is_available()
        assert expected_available_after == actual_available_after, "Book is not available"