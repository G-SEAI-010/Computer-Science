print("\n--- Listen erstellen und darauf zugreifen ---\n")

# Listen erstellen
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, [1, 2, 3]]
empty = []

# Zugriff über Index (nullbasiert)
print("erstes Element:", fruits[0])
print("drittes Element:", fruits[2])

# Negative Indexierung
print("letztes Element:", fruits[-1])
print("vorletztes Element:", fruits[-2])

# Länge der Liste
print("Länge:", len(fruits))

# Mitgliedschafts-Operatoren (Membership operators)
print("apple in fruits:", "apple" in fruits)
print("grape not in fruits:", "grape" not in fruits)

print("\n--- Listenelemente ändern ---\n")

colors = ["red", "green", "blue", "yellow"]
print("originale Liste:", colors)

# Einzelnes Element ändern
colors[1] = "purple"
print("nach einzelner Änderung:", colors)

# Mehrere Elemente mit Slicing ändern
colors[1:3] = ["orange", "pink"]
print("nach Slicing-Änderung:", colors)

# Durch eine andere Anzahl von Elementen ersetzen
colors[1:3] = ["cyan", "magenta", "lime"]
print("nach ungleichem Ersetzen:", colors)

print("\n--- Slicing von Listen ---\n")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("originale Liste:", numbers)

# Einfaches Slicing [Start:Ende] - Ende ist exklusiv (wird nicht eingeschlossen)
print("numbers[2:5]:", numbers[2:5])

# Start oder Ende weglassen
print("numbers[:4]:", numbers[:4])
print("numbers[5:]:", numbers[5:])

# Negative Index-Positionen beim Slicing
print("letzte 3:", numbers[-3:])
print("alle außer letzte 2:", numbers[:-2])

# Schritt-Parameter (Step) [Start:Ende:Schritt]
print("jedes 2.:", numbers[::2])
print("jedes 2. ab Index 1:", numbers[1::2])

print("\n--- Elemente zu Listen hinzufügen ---\n")

names = ["John", "Jane"]
print("originale Liste:", names)

# append() - am Ende hinzufügen
names.append("Jim")
print("nach append:", names)

# insert() - an einer bestimmten Position hinzufügen
names.insert(1, "Jan")
print("nach insert:", names)

# extend() - mehrere Elemente aus einem anderen Iterable hinzufügen
more_names = ["Jeremy", "James"]
names.extend(more_names)
print("nach extend:", names)

print("\n--- Elemente aus Listen entfernen ---\n")

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("originale Liste:", fruits)

# remove() - entfernt das erste Vorkommen des Wertes
fruits.remove("banana")
print("nach remove:", fruits)

# pop() - entfernt Element am Index (Standard: letztes Element)
fruits.pop()
print("nach pop:", fruits)

# del Schlüsselwort - löschen nach Index
del fruits[1]
print("nach del:", fruits)

# clear() - alle Elemente entfernen
fruits.clear()
print("nach clear:", fruits)

print("\n--- Durch Listen iterieren ---\n")

numbers = [2, 4, 6, 1, 3, 9]
print("originale Liste:", numbers)

# Einfache for-Schleife
for number in numbers:
    print("numbers:", number)

# Schleife, die eine neue Liste aufbaut
squared_numbers = []
for number in numbers:
    squared_numbers.append(number**2)

print("quadriert:", squared_numbers)

print("\n--- List Comprehension Grundlagen ---\n")

# new_list = [expression for item in iterable if condition]

numbers = [2, 4, 6, 1, 3, 9]
print("originale Liste:", numbers)

# Quadrate gerader Zahlen mithilfe von List Comprehension
numbers_squared = [number**2 for number in numbers if number % 2 == 0]
print("quadrierte gerade Zahlen:", numbers_squared)

# Strings in Großbuchstaben umwandeln
fruits = ["apple", "banana", "cherry"]
upper_fruits = [fruit.upper() for fruit in fruits]
print("Großbuchstaben:", upper_fruits)

print("\n--- Listen-Methoden ---\n")

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print("originale Liste:", numbers)

# count() - Vorkommen zählen
print("Anzahl der 1:", numbers.count(1))

# index() - erstes Vorkommen finden
print("Index der 4:", numbers.index(4))

# copy() - kopiert die Liste
print("Kopie:", numbers.copy())

# reverse() - Reihenfolge direkt in der Liste umkehren (in place)
numbers.reverse()
print("umgekehrt:", numbers)

# sort() - sortiert direkt in der Liste (modifiziert das Original)
numbers.sort()
print("aufsteigend sortiert:", numbers)

# sort() in absteigender Reihenfolge
numbers.sort(reverse=True)
print("absteigend sortiert:", numbers)
