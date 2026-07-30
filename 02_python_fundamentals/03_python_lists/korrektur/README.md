Exercises
=========

In this exercise, you will practice creating and manipulating lists. Follow the instructions step by step and test your code.

You can complete this exercise using the **online editor** or by downloading the script and working locally.

### Instructions

1.  **Create and Print a List**
    *   Create a list of 5 items (e.g., your favorite fruits, numbers, or any objects you like).
    *   Print the list to the screen.
2.  **Access Elements by Index and Negative Index**
    *   Print the first item, the last item, and at least one item using a negative index (for example, `my_list[-2]`).
3.  **Slice a List**
    *   Print a subset of the list (for example, items from index 1 to 3).
    *   Print everything from the beginning up to index 2, and from index 2 to the end.
4.  **Check if an Item Exists**
    *   Use the `in` keyword (for example, `if "apple" in my_list:`) to check if a certain item is in the list.
    *   Print a message indicating whether the item is found.
5.  **Add Items**
    *   Use `append()` to add a new item to the end of the list.
    *   Use `insert()` to add an item at a specific index.
6.  **Change Items**
    *   Update the value of a specific element by index.
    *   Change multiple items at once by assigning to a slice (for example, `my_list[1:3] = ["new1", "new2"]`).
7.  **Remove Items**
    *   Remove a specific item by value using `remove()`.
    *   Remove an item at a specific index using `pop()`.
    *   Clear the entire list with `clear()` (or demonstrate using a temporary list).
8.  **Copy a List**
    *   Create a copy of your list using `list.copy()` or slicing (`[:]`).
    *   Modify the original list afterward, then print both lists to verify they are independent.
9.  **Concatenate and Extend**
    *   Create two separate lists and join them in different ways:
        *   Using the `+` operator (e.g., `list_a + list_b`).
        *   Using `extend()` (e.g., `list_a.extend(list_b)`).
10.  **Sort and Reverse**
    *   Sort the list using `sort()`.
    *   Reverse the sorted list using `reverse()`.
    *   (Optional) Use `sorted()` to create a new sorted list without modifying the original.
11.  **Count and Index**
    *   Use `count()` to find how many times a particular value appears in the list.
    *   Use `index()` to find the position of a specific value in the list.
12.  **List Comprehension (Bonus)**
    *   Create a new list that transforms or filters your existing list (for example, convert strings to uppercase if they meet a certain condition).
    *   Use the syntax `[expression for item in my_list if condition]`.