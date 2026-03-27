# library

Design and implement a simple object-oriented system for managing books, users, and book loans in a library.

## Requirements

Books
•Each book has a title, author, category, and availability status.
•It should be possible to borrow and return a book.
•Attempting to borrow a book that is already loaned should be handled appropriately.

Users
•Each user has a name and can borrow multiple books.
•The user should be able to see which books they have borrowed.
•There should be a way to limit or validate certain user actions (e.g., borrowing too many books).

Library
•The library keeps track of all books and registered users.
•It should be possible to add new books and register new users.
•The library can list available books (i.e., not currently borrowed).
Book Types
•There should be at least one additional type of book that behaves differently (e.g., eBook or ReferenceBook).

Encapsulation and Validation
•Certain attributes (e.g., book title, user name, borrow status) should not be freely changeable.
•Proper access control and validation must be applied to sensitive attributes.

Reusability and Maintainability
•Follow object-oriented principles like inheritance and separation of concerns.
•Organize your code so it can be extended later (e.g., adding due dates or fines).

Deliverables:
•Python code with well-structured classes.
•Demonstration of functionality (can be simple print statements or test scenarios).
•Use meaningful names, documentation (docstrings), and readable formatting.
•Unit test mandatory

Bonus (Optional):
•Track how many books or users have been created in total.
•Add constraints (e.g., maximum 3 borrowed books per user).
•Allow search by author or category
