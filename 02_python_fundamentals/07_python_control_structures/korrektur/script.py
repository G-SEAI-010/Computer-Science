# 1. Basic If Condition
number = 0

if number > 0:
    print("'number' ist positiv")
elif number < 0:
    print("'number' ist negativ")
else:
    print("'number' ist null")

print()

# 2. Grade Calculator
score = 85

if score >= 90:
    print("Note: A")
elif score >= 80:
    print("Note: B")
elif score >= 70:
    print("Note: C")
elif score >= 60:
    print("Note: D")
else:
    print("Note: F")

# 3. Ternary Operator Practice
age = 15
status = "adult" if age >= 18 else "minor"
print("\nstatus:", status)


print()

# 4. For Loop over a List
vehicles = ["car", "bike", "plane"]
for vehicle in vehicles:
    print(f"Fahrzeug: {vehicle}")

print()

# 5. For Loop with Conditions
for number in range(1, 11):
    if number % 2 != 0:
        continue
    print("Gerade Zahl:", number)

print()

# 6. While Loop Summation
total = 0
count = 1

while count <= 100:
    total += count
    count += 1
print("Summer der Zahlen von 1 - 100", total)

print()

# 7. Break out of a Loop
words = ["hello", "dog", "word", "garden", "tent"]
for word in words:
    if len(word) > 5:
        print("Erstes Wort mit mehr als 5 Buchstaben:", word)
        break

print()

# 8. Nested Loops
people = ["John", "Jane", "Joe"]
pets = ["cat", "dog", "bird"]

for person in people:
    for pet in pets:
        print(f"{person} + {pet}")

print()

# 9. Loop with Else Clause
haystack = [
    "test",
    "cat",
    "needle",
    "january",
    "home",
]
needle = "needle"
for word in haystack:
    if word == needle:
        print("Element wurde gefunden")
        break
else:
    print(f"'{needle}' konnte nicht gefunden werden")

print()

# 10. Pass Statement Usage
items = ["apple", "banana", "cherry"]
for item in items:
    pass  # Platzhalter

# 11. Pattern matching
fruits = ["apple", "banana", "orange", "mango"]
veggies = ["carrot", "broccoli", "spinach", "pepper"]
meat = ["chicken", "beef", "pork", "lamb"]
item = "mango"

match item:
    case _ if item in fruits:
        print(f"'{item}' kommt in 'fruits' vor")
    case _ if item in veggies:
        print(f"'{item}' kommt in 'veggies' vor")
    case _ if item in meat:
        print(f"'{item}' kommt in 'meat' vor")
    case _:
        print(f"'{item}' kann keiner Kategorie zugeordnet werden")
