Exercises
=========

**In this exercise, you will practice creating and manipulating Python dictionaries using various methods.** Follow the instructions step by step and test your code.

You can complete this exercise using the online editor or by downloading the script and working locally.

### Instructions

1.  **Create and Print a Dictionary**
    *   Create a dictionary representing a person with keys such as `"name"`, `"age"`, and `"city"`.
    *   Print the entire dictionary to the screen.
2.  **Access Dictionary Elements**
    *   Print the value associated with the key `"name"` using square brackets.
    *   Use the `get()` method to safely retrieve the value for a key that might not exist (e.g., `"email"`), providing a default value.
    *   Print all keys, values, and items of the dictionary using `keys()`, `values()`, and `items()` methods.
3.  **Check for Key Existence**
    *   Check if the key `"age"` exists in the dictionary using the `in` keyword.
    *   Print a message based on whether the key is found or not.
4.  **Change and Update Dictionary Elements**
    *   Update the value associated with `"city"` directly by assignment.
    *   Use the `update()` method to change multiple key-value pairs or add new ones (e.g., add `"occupation": "Engineer"`).
5.  **Add New Items to the Dictionary**
    *   Add a new key-value pair (e.g., `"country": "USA"`) using direct assignment.
    *   Use `update()` to add another new key-value pair (e.g., `"hobby": "cycling"`).
6.  **Remove Items from the Dictionary**
    *   Remove an item by key using `pop()` and print the removed value.
    *   Use `popitem()` to remove the last inserted key-value pair, and print the pair removed.
    *   Delete a specific key-value pair using the `del` keyword.
    *   Clear the entire dictionary using `clear()` and print the empty dictionary.
7.  **Copy a Dictionary**
    *   Create a shallow copy of your dictionary using the `copy()` method or `dict()` constructor.
    *   Modify the original dictionary and show that the copy remains unchanged.
8.  **Using setdefault()**
    *   Use `setdefault()` to retrieve the value of a key that exists, and then for a key that doesn’t exist, adding it with a default value.
    *   Print the dictionary to observe changes.