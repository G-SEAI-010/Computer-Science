print(
    "--- Bedingte Anweisungen (Conditionals) & Ternärer Operator (Ternary Operator) ---\n"
)

# if/else Statement
score = 85
if score >= 90:
    print("Note:", "A")
elif score >= 80:
    print("Note:", "B")
elif score >= 70:
    print("Note:", "C")
else:
    print("Note:", "F")


# Ternärer Operator
age = 17
status = "teenager" if age >= 13 and age <= 19 else "other"

if age >= 18:
    status = "adult"
elif age >= 13:
    status = "teenager"
else:
    status = "child"

print("\n--- For- und While-Schleifen ---\n")

vehicles = ["car", "bike", "plane"]

# for Schleife
for vehicle in vehicles:
    print("Fahrzeug:", vehicle)

print()

# range (Bereich) mit Schrittweite (step)
for i in range(0, 10, 2):
    print("gerade Zahl:", i)

print()

# while Schleife mit break und continue
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # Wenn count eine gerade Zahl ist, wird der Durchgang übersprungen
    if count > 7:
        break  # Schleife wird abgebrochen, wenn count > 7
    print("ungerade Zahl:", count)

print("\n--- Schleifen-Else und Pattern Matching ---\n")

# else wird nur ausgeführt, wenn die Schleife NICHT durch break abgebrochen wurde
haystack = ["cat", "needle", "dog"]
for word in haystack:
    if word == "needle":
        print("Gefunden:", word)
        break

else:
    print("Ergebnis:", "Nicht gefunden")

# Pattern Matching mit Bedingungen (Guards) (Python 3.10+)

fruits = ["apple", "banana", "mango"]
veggies = ["carrot", "broccoli"]
meat = ["chicken", "beef"]

item = "mango"

match item:
    case _ if item in fruits:
        print("Kategorie:", "fruits")
    case _ if item in veggies:
        print("Kategorie:", "veggies")
    case _ if item in meat:
        print("Kategorie:", "meat")
    case _:
        print("Kategorie:", "unknown")

# Zum Vergleich mit einem if/else Statement:
# item = "mango"

# if item in fruits:
#     print("Kategorie:", "fruit")
# elif item in veggies:
#     print("Kategorie:", "veggies")
# elif item in meat:
#     print("Kategorie:", "meat")
# else:
#     print("Kategorie:", "unknown")
