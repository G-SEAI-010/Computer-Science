print("\n--- Dictionaries erstellen ---\n")

# Dictionaries mit geschweiften Klammern erstellen
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
}

# Leeres Dictionary
empty = {}
print("\nTyp von empty:", type(empty))

# Verwendung des dict() Konstruktors
person2 = dict(name="Bob", age=30, city="London")
print("\nperson2:", person2)

print("\n--- Auf Dictionary-Elemente zugreifen ---\n")

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "email": "alice@email.com",
}

# Zugriff über eckige Klammern - Stürzt mit Fehler ab, wenn der Schlüssel nicht existiert
print("\nName:", person["name"])
print("Alter:", person["age"])

# Sicherer Zugriff über get() - Stürzt NICHT ab, wenn der Schlüssel fehlt
print("\nE-Mail:", person.get("email"))
print("Telefon:", person.get("phone"))

# .get() - lässt dich einen Standard-Rückgabewert (Fallback) festlegen:
print("\nTelefon Standardwert:", person.get("phone", "Nicht angegeben"))

# Alle Schlüssel abrufen
print("\nSchlüssel (keys):", list(person.keys()))

# Alle Werte abrufen
print("\nWerte (values):", list(person.values()))

# Alle Schlüssel-Wert-Paare abrufen
print("\nPaare (items):", list(person.items()))

print("\n--- Dictionary-Elemente ändern ---\n")

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
}

# Vorhandenen Wert ändern
person["age"] = 26
print("Nach Alters-Update:", person)

# Neues Schlüssel-Wert-Paar hinzufügen
person["color"] = "Green"
print("\nNach Hinzufügen der Farbe:", person)

# Mehrere Einträge auf einmal hinzufügen oder aktualisieren
person.update(
    {
        "age": 27,
        "phone": "555-1234",
        "country": "USA",
    }
)
print("\nNach update():", person)

# setdefault() - fügt Element nur hinzu, wenn der Schlüssel noch NICHT existiert
# person.setdefault("name", "John")
# print("\nname (unverändert):", person["name"])

person.setdefault("test", "Wert")
print("\ntest (hinzugefügt):", person["test"])

print("\n--- Elemente aus Dictionaries entfernen ---\n")

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "email": "alice@email.com",
    "phone": "555-1234",
}

# pop() - Wert entfernen und zurückgeben - Gibt einen Fehler aus, wenn Schlüssel fehlt
person.pop("email")
print("Nach pop:", person)

# pop() mit Standardwert (Fallback) - Gibt keinen Fehler zurück, wenn Schlüssel fehlt
# person.pop("mobile", "Nicht gefunden")

# popitem() - Das letzte Element entfernen und zurückgeben
last_item = person.popitem()
print("\npopitem:", last_item)

# del Schlüsselwort - einen bestimmten Schlüssel löschen
del person["city"]
print("\nNach del city:", person)

# clear() - alle Elemente entfernen
person.clear()
print("\nNach clear:", person)

print("\n--- Durch Dictionaries iterieren ---\n")

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "email": "alice@email.com",
}

# Durch Schlüssel-Wert-Paare iterieren
for key, value in person.items():
    print(f"  {key}: {value}")

# Mit enumerate für eine Nummerierung
# for index, (key, value) in enumerate(person.items(), start=1):
#     print(f"  {index}. {key}: {value}")

print("\n--- Dictionaries kopieren ---\n")

# FALSCHER WEG - erstellt nur eine Referenz, keine echte Kopie
# original = {
#     "name": "Alice",
#     "age": 25,
# }
# reference = original
# reference["age"] = 30
# print("original (verändert!):", original)

# RICHTIGER WEG - copy() verwenden (Flache Kopie / Shallow Copy)
original = {
    "name": "Alice",
    "age": 25,
}
copy1 = original.copy()
copy1["age"] = 30
print("original (unverändert):", original)
print("copy1:", copy1)

# WARNUNG ZUR FLACHEN KOPIE - verschachtelte Objekte werden weiterhin nur referenziert!
# original = {
#     "name": "Alice",
#     "scores": [85, 90, 95],
# }
# shallow = original.copy()
# shallow["scores"].append(100)
# print("original scores (verändert!):", original["scores"])

# TIEFE KOPIE (DEEP COPY) - für verschachtelte Strukturen
# import copy  # Koventionell imports am Anfang der Datei

# original = {
#     "name": "Alice",
#     "scores": [85, 90, 95],
# }
# deep = copy.deepcopy(original)
# deep["scores"].append(100)
# print("original scores (sicher):", original["scores"])
# print("deep scores (Kopie):", deep["scores"])

print("\n--- Verschachtelte Dictionaries ---\n")

users = {
    "user1": {"name": "Alice", "age": 25, "email": "alice@email.com"},
    "user2": {"name": "Bob", "age": 30, "email": "bob@email.com"},
    "user3": {"name": "Charlie", "age": 35, "email": "charlie@email.com"},
}

# Auf verschachtelte Werte zugreifen
print("user1 name:", users["user1"]["name"])
print("user2 age:", users["user2"]["age"])

# Sicherer Zugriff durch das Verketten von get()
# email = users.get("user1", {}).get("email", "Keine E-Mail")
# print("\nuser1 email:", email)

# phone = users.get("user1", {}).get("phone", "Kein Telefon")
# print("user1 Telefon:", phone)

print()

# Durch verschachtelte Dictionaries iterieren
for user_id, user_info in users.items():
    print(f"  {user_id}:")
    for key, value in user_info.items():
        print(f"    {key}: {value}")

print("\n--- Dictionaries zusammenfügen (Merging) ---\n")

# Python 3.9+ - mit dem | Operator
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2
print("Zusammengefügt:", merged)

# Überlappende Schlüssel - das zweite Dictionary überschreibt das erste
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = dict1 | dict2
print("\nÜberlappend:", merged)

# Mit ** Unpacking (Python 3.5+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print("\nEntpackt zusammengefügt:", merged)

# Mehrere Dictionaries zusammenfügen
d1 = {"a": 1}
d2 = {"b": 2}
d3 = {"c": 3}
merged = {**d1, **d2, **d3}
print("\nMehrfach-Merge:", merged)
