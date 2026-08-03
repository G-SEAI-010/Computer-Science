Exercises
=========

**In this exercise, you will practice creating and manipulating Python sets.** Follow the instructions step by step and test your code.

You can complete this exercise using the online editor or by downloading the script and working locally.

### Instructions

1.  **Create a Set**
    *   Create a set named `fruits` containing at least 5 unique items (e.g., names of fruits).
    *   Print the set.
2.  **Check Membership**
    *   Check if a specific item (e.g., `"apple"`) is in `fruits` using the `in` keyword and print a message confirming its presence or absence.
3.  **Add and Update Items**
    *   Add a new element to `fruits` using the `add()` method. Print the set after adding.
    *   Create another set `more_fruits` with at least 3 unique items.
    *   Use the `update()` method to add elements from `more_fruits` to `fruits`. Print the updated set.
4.  **Remove Items**
    *   Remove an element from `fruits` using `remove()`. Print the set after removal.
    *   Attempt to remove an element not in the set using `discard()` and observe that no error occurs.
    *   Use `pop()` to remove and print an arbitrary element from `fruits`. Then print the set.
    *   Use `clear()` to remove all elements from a copy of `fruits` and print the empty set.
5.  **Set Operations**
    *   Create two sets:
        *   `set_a` with some overlapping items with `fruits`.
        *   `set_b` with some different items.
    *   Perform and print the result of the following operations:
        *   **Union**: Use `union()` to combine `set_a` and `set_b`.
        *   **Intersection**: Use `intersection()` to find common elements between `set_a` and `set_b`.
        *   **Difference**: Use `difference()` to find elements in `set_a` not in `set_b`.
        *   **Symmetric Difference**: Use `symmetric_difference()` to find items in either `set_a` or `set_b` but not in both.
6.  **In-place Set Operations**
    *   Use `difference_update()` on a set to remove items that are also in another set. Print the result.
    *   Use `intersection_update()` on a set to keep only items common with another set. Print the result.
    *   Use `update()` to add elements from another set to the current set. Print the result.
7.  **Relational Methods**
    *   Create two sets `small_set` and `large_set` such that `small_set` is a subset of `large_set`.
    *   Use `issubset()` to verify that `small_set` is a subset of `large_set` and print the result.
    *   Use `issuperset()` to verify that `large_set` is a superset of `small_set` and print the result.
    *   Check if two sets are disjoint using `isdisjoint()` and print the result.