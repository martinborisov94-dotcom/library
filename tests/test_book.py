
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
