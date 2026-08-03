#  1. Create a Set
fruits = {"apple", "banana", "cherry", "mango", "kiwi"}
print("fruits:", fruits)

# 2. Check Membership
if "apple" in fruits:
    print("'apple' ist in fruits")

# 3. Add and Update Items
fruits.add("grape")
print("\nNach add:", fruits)

more_fruits = {"pear", "plum", "peach"}
fruits.update(more_fruits)
print("\nNach update:", fruits)

# 4. Remove Items
fruits.remove("kiwi")
print("\nNach remove:", fruits)

fruits.discard("dragonfruit")

popped = fruits.pop()
print("\npopped Element:", popped)
print("Nach pop:", fruits)

fruits.clear()
print("\nNach clear:", fruits)

# 5. Set Operations
set_a = {"apple", "banana", "cherry", "orange"}
set_b = {"orange", "grape", "melon"}

print("\nunion:", set_a.union(set_b))
print("intersection:", set_a.intersection(set_b))
print("difference:", set_a.difference(set_b))
print("symmetric difference:", set_a.symmetric_difference(set_b))

# 6. In-place Set Operations
set_c = {"apple", "banana", "cherry", "orange"}
set_c.difference_update(set_b)
print("\nNach difference_update:", set_c)

set_d = {"apple", "banana", "cherry", "orange"}
set_d.intersection_update({"apple", "banana", "melon"})
print("\nNach intersection_update:", set_d)

set_e = {"apple", "banana"}
set_e.update({"cherry", "mango"})
print("\nNach update:", set_e)

# 7. Relational Methods
small_set = {"apple", "banana"}
large_set = {"apple", "banana", "cherry", "mango"}

print("\nissubset:", small_set.issubset(large_set))
print("issuperset:", large_set.issuperset(small_set))

unrelated_set = {"grape", "melon"}
print("issuperset:", unrelated_set.isdisjoint(small_set))
