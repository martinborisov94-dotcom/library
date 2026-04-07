"""Main file of the library management system."""

from src.book import Book
from src.library import Library
from src.user import User

def main():
    """Main function of the program."""
    print("Hello, welcome to the library management system!")

    library = Library()
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "first_category")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "second_category")
    book3 = Book("1984", "George Orwell", "third_category")
    book4 = Book("The Catcher in the Rye", "J.D. Salinger", "fourth_category")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

    user1 = User("Martin")
    user2 = User("Pesho")

    library.register_user(user1)
    library.register_user(user2)

    print("Available books in the library:" + str(library.get_available_books()))
    print("All users in the library:" + str(library.get_all_users()))


    user1.add_borrowed_book(book1)
    user1.add_borrowed_book(book2)
    user2.add_borrowed_book(book3)
    print("Available books in the library after borrowing:" + str(library.get_available_books()))
    user1.remove_borrowed_book(book1)
    print("Available books in the library after returning:" + str(library.get_available_books()))



# This ensures the code runs only when executed directly, not when imported
if __name__ == "__main__":
    main()
