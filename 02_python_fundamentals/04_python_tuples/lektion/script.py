print("\n--- Tupel erstellen ---\n")

# Tupel mit runden Klammern erstellen
fruits = ("apple", "banana", "cherry")
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)

# Tupel ohne Klammern (Packing)
coordinates = 10, 20, 30
print("Typ von coordinates:", type(coordinates))

# Leeres Tupel
empty = ()

# Verwendung des tuple() Konstruktors
from_list = tuple([1, 2, 3])
from_string = tuple("hello")
print("Aus Liste:", type(from_list))
print("Aus String:", from_string)

print("\n--- Auf Tupel-Elemente zugreifen ---\n")

colors = ("red", "green", "blue", "yellow", "purple")

# Positive Indexierung
print("Erstes Element:", colors[0])

# Negative Indexierung
print("Letztes Element:", colors[-1])

# Länge
print("Länge:", len(colors))

# Mitgliedschaft prüfen
print("'green' in colors:", "green" in colors)
print("'orange' not in colors:", "orange" not in colors)

print("\n--- Slicing von Tupeln ---\n")

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Einfaches Slicing [Start:Ende]
print("numbers[2:5]:", numbers[2:5])

# Start oder Ende weglassen
print("numbers[:4]:", numbers[:4])
print("numbers[5:]:", numbers[5:])

# Negative Indizes
print("Letzte 3:", numbers[-3:])
print("Alle außer die letzten 2:", numbers[:-2])

# Schritt-Parameter (Step)
print("Jedes 2.:", numbers[::2])
print("Jedes 2. ab Index 1:", numbers[1::2])

print("\n--- Tupel-Unveränderlichkeit ---\n")

coordinates = (10, 20, 30)

# Tupel können nicht verändert werden
# coordinates[0] = 15          # TypeError!
# coordinates.append(40)       # AttributeError!

coordinates = (15, 25, 35)
print("Neu zugewiesen:", coordinates)

print("\n--- Tupel-Methoden ---\n")

numbers = (1, 2, 3, 2, 4, 2, 5, 6, 2)

# count() - Vorkommen zählen
print("Anzahl der 2:", numbers.count(2))

# index() - erstes Vorkommen finden
print("Index der 3:", numbers.index(3))

# index() mit Start- und End-Parametern
print("Index der 2 nach Pos. 2:", numbers.index(2, 2))
print("Index der 2 zwischen 4-8:", numbers.index(2, 4, 8))

print("\n--- Einfaches Tupel-Unpacking ---\n")

# In Variablen entpacken (Unpacking)
point = (10, 20)
x, y = point
print(f"x = {x}, y = {y}")

# RGB-Farbe
color = (255, 128, 0)
red, green, blue = color
print(f"\nR:{red} G:{green} B:{blue}")

print("\n--- Unpacking mit Sternchen ---\n")

# Restliche Elemente sammeln
numbers = (1, 2, 3, 4, 5)
first, *rest = numbers
print("first:", first)
print("rest:", rest)

# Sternchen in der Mitte
first, *middle, last = numbers
print("\nfirst:", first)
print("middle:", middle)
print("last:", last)

# Sternchen am Anfang
*beginning, second_last, last = numbers
print("\nbeginning:", beginning)
print("second_last:", second_last)
print("last:", last)

print("\n--- Tupel zusammenfügen - Verkettung ---\n")

# Verwendung des + Operators
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print("Kombiniert:", combined)

# Ursprüngliche Tupel bleiben unverändert
print("tuple1:", tuple1)
print("tuple2:", tuple2)

# Einzelnes Element hinzufügen (muss ein Tupel sein!)
fruits = ("apple", "banana")
more_fruits = fruits + ("cherry",)
print("more_fruits:", more_fruits)

print("\n--- Tupel zusammenfügen - Multiplikation ---\n")

# Tupel mehrfach wiederholen
base = (1, 2, 3)
repeated = base * 3
print("wiederholt:", repeated)

# Praktische Anwendung: Mit Standardwerten initialisieren
zeros = (0,) * 50
print("Nullen:", zeros)

# Muster erstellen
pattern = ("X", "O") * 4
print("Muster:", pattern)

print("\n--- Durch Tupel iterieren ---\n")

colors = ("red", "green", "blue", "yellow")

# Einfache for-Schleife
for color in colors:
    print("Farbe:", color)

print()

# Mit enumerate() für den Index
for index, color in enumerate(colors):
    print(f"{index}: {color}")
