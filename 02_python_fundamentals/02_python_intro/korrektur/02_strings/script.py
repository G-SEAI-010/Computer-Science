# Step 1: Create Strings
first_name = "Testy"
last_name = "McTest"
bio = """Ich bin eine reale Person.
Glaub mir!
Ich kann mit Python programmieren.
"""

# Step 2: Access Characters and Slice Strings
print("Erster Charakter:", first_name[0])
print("Letzter Charakter:", first_name[-1])
print("Erste 10 Charaktere:", bio[0:10], "\n")

# Step 3: Loop Through a String
for character in first_name:
    print("Charakter:", character)

# Step 4: String Length
print("\nLänge von bio:", len(bio))

# Step 5: Check Substrings
print("\n'Python' in bio:", "Python" in bio)
print("'Java' nicht in bio:", "Java" not in bio)

# Step 6: Modify Strings
print("\nGroßbuchstaben:", first_name.upper())
print("Kleinbuchstaben:", last_name.lower())
print("Ohne Leerzeichen:", bio.strip())
print("Ersetzen:", bio.replace("Python", "Java"))
print("Aufteilen:", bio.split())

# Step 7: Concatenate Strings
full_name = first_name + " " + last_name
print("\nfull_name:", full_name)

# Step 8: String Formatting
print(f"\nHallo, mein Name ist {full_name} und ich mag Python!")
print("Hallo, mein Name ist {} und ich bin {} Jahre alt.".format(full_name, 30))

# Step 9: Escape Characters
quote = 'Er sagte:"Python ist gut!"'
print("\nquote:", quote)

# Bonus: Use String Methods
print("\nZentrierter full_name: ", full_name.center(50))
print("'t' in full_name zählen:", full_name.count("t"))
