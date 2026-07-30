# Step 1: Create and Print a List
numbers = [1, 2, 3, 4, 5]
print("numbers Liste:", numbers)

# Step 2: Access Elements by Index and Negative Index
print("\nErstes Element:", numbers[0])
print("Letztes Element:", numbers[-1])
print("Vorletztes Element:", numbers[-2])

# Step: 3 Slice a List
print("\nIndex 1 bis 3:", numbers[1:3])
print("Anfang bis Index 2:", numbers[0:2])
print("Index 2 bis Ende:", numbers[2:])

# Step 4: Check if an Item Exists
if 5 in numbers:
    print("\nNummer 5 ist in der Liste vorhanden.")

# Step 5: Add Items
numbers.append(6)
numbers.insert(0, 0)
print("\nNach append und insert:", numbers)

# Step 6: Change Items
numbers[6] = 7
numbers[0:2] = [-1, 0]
print("\nNach den Änderungen:", numbers)

# Step 7: Remove items
numbers.remove(3)
numbers.pop(1)
print("\nNach remove und pop:", numbers)

numbers_2 = [0, 1, 2]
numbers_2.clear()
print("\nNach clear (temporäre Liste):", numbers_2)

# Step 8: Copy a list
numbers_copy = numbers.copy()
numbers.insert(0, -2)
print("\nOriginal nach Modifikation:", numbers)
print("Kopie unberührt:", numbers_copy)

# Step 9: Concatenate and Extend
my_list_1 = ["apple", "cherry"]
my_list_2 = ["orange", "banana"]
print("\nKonkateniert:", my_list_1 + my_list_2)
my_list_1.extend(my_list_2)
print("Erweitert:", my_list_1)

# Step 10: Sort and Reverse
my_list_1.sort()
print("\nSortiert:", my_list_1)
my_list_1.reverse()
print("Umgekehrt:", my_list_1)
my_list_1_sorted = sorted(my_list_1)
print("Sortierte Kopie:", my_list_1_sorted)

# Step 11: Count and Index
print("\nAnzahl von 'apple':", my_list_1.count("apple"))
print("Index von 'cherry':", my_list_1.index("cherry"))

# Step 12: List comprehension
uppercase_list = [fruit.upper() for fruit in my_list_1 if len(fruit) == 6]
print("\nElemente mit 6 Charakteren in Großbuchstaben:", uppercase_list)
