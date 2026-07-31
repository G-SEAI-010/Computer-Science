# 1. Create a Tuple
my_tuple = ("apple", "banana", "cherry", "mango", "kiwi", "cherry")

# 2. Print the Tuple
print("my_tuple:", my_tuple)

# 3. Access Tuple Items
print("\nErstes Element:", my_tuple[0])
print("Letztes Element:", my_tuple[-1])

# 4. Slice the Tuple
print("\nMittlere Elemente:", my_tuple[1:4])
print("Start bis Index 3:", my_tuple[:3])
print("Index 3 bis Ende:", my_tuple[3:])

# 5. Check if an Item Exists
if "mango" in my_tuple:
    print("\n'mango' ist in tuple")
else:
    print("\n'mango' ist nicht in tuple")

# 6. Count and Index
print("\nAnzahl von 'cherry':", my_tuple.count("cherry"))
print("Index von 'cherry':", my_tuple.index("cherry"))

# 7. Packing and Unpacking
first, second, third, fourth, fifth, sixth = my_tuple
print("\nunpacked:", first, second, third, fourth, fifth, sixth)

first, *middle, last = my_tuple
print("\nfirst:", first)
print("middle:", middle)
print("last:", last)

# 8. Joining Tuples
another_tuple = ("grape", "pear", "plum")
combined_tuple = my_tuple + another_tuple
print("\nconcatenated:", combined_tuple)
print("\nmultiplied:", another_tuple * 2)
