print("\n--- Sets erstellen ---\n")

# Sets mit geschweiften Klammern erstellen
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14, True, (1, 2, 3)}

# Leeres Set - MUSS set() verwenden, nicht {}
empty = set()
empty_dict = {}  # Das ist ein DICT, kein Set!
print("Typ von empty:", type(empty))
print("Typ von not_empty:", type(empty_dict))

# Verwendung des set() Konstruktors
from_string = set("hello")
print("\nfrom_string:", from_string)

# Kann nicht indiziert oder gesliced werden
# numbers[0]  # TypeError: 'set' object is not subscriptable

# Zugehörigkeitsprüfung ist sehr effizient (Hash-Table)
print("\n'1' in numbers:", 1 in numbers)
print("'7' nicht in numbers:", 7 not in numbers)

# Längeneigenschaft
print("\nLänge von numbers:", len(numbers))

print("\n--- Elemente hinzufügen ---\n")

fruits = {"apple", "banana"}

# add() - einzelnes Element hinzufügen
fruits.add("cherry")
print("Nach add:", fruits)

# Das Hinzufügen eines Duplikats hat keinen Effekt
fruits.add("apple")
print("\nNach Hinzufügen eines Duplikats:", fruits)

# update() - mehrere Elemente aus einem Iterable hinzufügen
fruits.update(["date", "elderberry"])
print("\nNach update:", fruits)

# update() mit mehreren Iterables
fruits.update(["fig"], ("grape",), {"honeydew"})
print("\nNach Mehrfach-update:", fruits)

print("\n--- Elemente entfernen ---\n")

colors = {"red", "green", "blue", "yellow", "purple"}

# remove() - entfernt Element, löst KeyError aus, wenn nicht gefunden
colors.remove("blue")
print("Nach remove:", colors)

# discard() - entfernt Element, KEIN Fehler, wenn nicht gefunden
colors.discard("black")
print("\nNach discard:", colors)

# pop() - entfernt ein beliebiges Element und gibt es zurück
removed = colors.pop()
print("\nEntfernt:", removed)
print("Nach pop:", colors)

# clear() - alle Elemente entfernen
colors.clear()
print("\nNach clear:", colors)

print("\n--- Durch Sets iterieren ---\n")

fruits = {"apple", "banana", "cherry", "date"}

# Einfache for-Schleife (Reihenfolge nicht garantiert)
for fruit in fruits:
    print("Frucht:", fruit)

print("\n--- Set-Vereinigung (Union) ---\n")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# union() Methode => nicht-mutierend (verändert Original nicht)
result = set_a.union(set_b)
print("\nunion():", result)

# | Operator (Kurzschreibweise)
result = set_a | set_b
print("\na | b:", result)

# Vereinigung mit mehreren Sets
set_c = {7, 8}
result = set_a | set_b | set_c
print("\na | b | c:", result)

# |= Operator (In-place union) => mutierend
set_x = {1, 2, 3}
set_y = {3, 4, 5}
set_x |= set_y
print("\nx |= y:", set_x)

print("\n--- Set-Schnittmenge (Intersection) ---\n")

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

# intersection() Methode
common = set_a.intersection(set_b)
print("intersection():", common)

# & Operator (Kurzschreibweise)
print("\na & b:", set_a & set_b)

# Schnittmenge mit mehreren Sets
set_c = {4, 5, 8, 9}
print("\na & b & c:", set_a.intersection(set_b, set_c))

# &= Operator (In-place intersection)
set_x = {1, 2, 3, 4}
set_y = {3, 4, 5, 6}
set_x &= set_y
print("\nx &= y:", set_x)

print("\n--- Set-Differenz (Difference) ---\n")

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

# difference() Methode
different = set_a.difference(set_b)
print("difference():", different)

# - Operator (Kurzschreibweise)
print("\na - b:", set_a - set_b)

# Differenz mit mehreren Sets
set_c = {2, 5, 8}
print("\na - b - c:", set_a.difference(set_b, set_c))

# -= Operator (In-place difference)
set_x = {1, 2, 3, 4, 5}
set_y = {3, 4, 5}
set_x -= set_y
print("\nx -= y:", set_x)

print("\n--- Set-Beziehungen ---\n")

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
set_c = {6, 7, 8}

# a.issubset(b) → "Ist alles in a auch in b?"
print("a Teilmenge von b:", set_a.issubset(set_b))
print("b Teilmenge von a:", set_b.issubset(set_a))

# a <= b → selbe wie issubset — ist a in b (oder gleich groß)?
print("\na <= b:", set_a <= set_b)

# a < b → "echte Teilmenge" (strict subset) — ist a in b UND nicht exakt gleich b?
print("\na < b (echte):", set_a < set_b)
print("a < a:", set_a < set_a)

# a.issuperset(b) → "Ist alles in b auch in a?"
print("\na Obermenge von b:", set_a.issuperset(set_b))
print("b >= a:", set_b >= set_a)

# a.isdisjoint(c) → "Haben diese beiden Sets keine gemeinsamen Elemente?"
print("\na disjunkt zu c:", set_a.isdisjoint(set_c))
print("a disjunkt zu b:", set_a.isdisjoint(set_b))
