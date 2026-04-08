
""" Unit tests for User class."""

from src.user import User


class TestUser():
    """ Unit test for User class."""

    def test_user_initial_state_name_and_borrowed_list(self):
        """Test get name function"""
        expected_name = "Jane Doe"
        user = User(expected_name)
        actual_name = user.get_name()
        assert actual_name == expected_name

    def test_borrowed_list(self):
        """Test borrowed list"""
        expected_name = "Jane Doe"
        user = User(expected_name)
        actual_borrowed = user.get_borrowed_books()
        assert actual_borrowed == []

    def test_user_equality_same_name(self):
        """Test two users with same names"""
        user1 = User("Bob")
        user2 = User("Bob")
        expected_equal = True
        actual_equal = (user1 == user2)
        assert expected_equal == actual_equal

    def test_user_equality_different_name_and_other_type(self):
        """Test users with different names"""
        user1 = User("Bob")
        user2 = User("Charlie")
        expected_equal = False
        actual_equal = (user1 == user2)
        assert expected_equal == actual_equal
