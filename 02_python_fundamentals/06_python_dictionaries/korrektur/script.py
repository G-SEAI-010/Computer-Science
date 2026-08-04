# 1. Create and Print a Dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "Berlin",
}
print("person:", person)


# 2. Access Dictionary Elements
print("\nname:", person["name"])
print("email:", person.get("email", "E-Mail nicht vorhanden"))
print("keys:", person.keys())
print("values:", person.values())
print("items:", person.items())

# 3. Check for Key Existence
if "age" in person:
    print("\n'age' Schlüssel existiert")

# 4. Change and Update Dictionary Elements
person["city"] = "Munich"
person.update({"occupation": "Engineer", "age": 31})
print("\nNach Änderungen:", person)

# 5. Add New Items to the Dictionary
person["country"] = "Germany"
person.update({"hobby": "cycling"})
print("\nNach hinzufügen:", person)

# 6. Remove Items from the Dictionary
removed = person.pop("occupation")
print("\nremoved:", removed)

last_item = person.popitem()
print("\npopitem:", last_item)

del person["country"]
print("\nNach del:", person)

person_copy_for_clear = person.copy()
person_copy_for_clear.clear()
print("\nNach clear:", person_copy_for_clear)

# 7. Copy a Dictionary
person_copy = person.copy()
person["city"] = "Hamburg"
print("\nOriginal nach modifizierung:", person)
print("Kopie unverändert:", person_copy)

# 8. Using setdefault()
print("\nsetdefault exisiterender Schlüssel:", person.setdefault("name", "unknown"))
print("setdefault neuer Schlüssel:", person.setdefault("email", "alice@example.com"))
print("Nach setdefault:", person)
