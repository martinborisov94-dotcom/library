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

## Installation

1. To install venv -> python -m venv .venv
2. Create requirements.txt for the dependencies -> echo . > requirements.txt
or pip freeze > requirements.txt
3. Add Pylint to requirements.txt
4. Add coverage to requirements.txt

## Usage

1. To activate .venv -> .venv\Scripts\activate
2. To deactivate .venv -> deactivate
3. To install all packages from requirements.txt, run: python -m pip install -r requirements.txt
4. To run module with pylint-> pylint .\src\string_tasks.py
5. Run coverage -> coverage run --source=src --omit="*/init.py" -m unittest tests.test_my_math
6. Generate html report -> coverage html
7. To run pytest -> python -m pytest -v