Exercises
=========

**In this exercise, you will practice creating custom classes to model a simple book collection.** Follow the instructions step by step and test your code.

You can complete this exercise using the online editor or by downloading the script and working locally.

### Instructions

1.  **Create a `Book` Class**
    
    *   Define a class named `Book`.
    *   The `Book` class should have an `__init__()` method that takes parameters for the book's `name`, `author`, and `release_date`.
    *   Store these parameters as attributes of the instance.
    *   Optionally, include a boolean attribute `read` initialized to `False` to track if the book has been read.
2.  **Create a `BookCollection` Class**
    
    *   Define a class named `BookCollection`.
    *   In the `__init__()` method, initialize the books to a list of books passed to the constructor or an empty list.
    *   If you pass a list, verify its elements are indeed instances of a `Book` otherwise, raise and exception.
3.  **Add Books to the Collection**
    
    *   Within the `BookCollection` class, create a method `add_book(self, book)` that takes a `Book` object as a parameter and adds it to the collection (`self.books`).
    *   Verify every new entry is indeed an instance of `Book` otherwise, raise and exception.
4.  **Mark Books as Read**
    
    *   In the `BookCollection` class, implement a method `mark_as_read(self, book_name)` that:
        *   Searches for a book by its name in the collection.
        *   If found, sets its `read` attribute to `True`.
        *   If not found, optionally prints a message indicating the book isn't in the collection.
5.  **Display Collection Status**
    
    *   Optionally, add a method `list_books(self)` in `BookCollection` that prints out all the books with their details and read status.