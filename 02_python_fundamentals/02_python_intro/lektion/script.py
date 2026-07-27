print("\n--- Python-Syntax und erstes Programm ---\n")

# Variablendeklaration - kein Typ erforderlich!
name = "Alice"

# Die print()-Funktion zeigt die Ausgabe an
print("Das ist mein erster print:", name)

"""
Dies ist ein mehrzeiliger Kommentar.
Du kannst hier mehrere Zeilen schreiben.
Nützlich für Dokumentationen!
"""

print("\n--- Variablen und Typenprüfung ---\n")

# Variablen mit verschiedenen Typen erstellen
student_name = "Bob"
is_enrolled = True

# Den Typ jeder Variable überprüfen
print("Typ von student_name:", type(student_name))
print("Typ von is_enrolled:", type(is_enrolled))

# Variablen können neu zugewiesen werden mit anderen Typen (dynamische Typisierung)
my_variable = 10
print(my_variable, type(my_variable))
my_variable = "Hallo"
print(my_variable, type(my_variable))

x, y, z = 1, 2, 3
print("x:", x)
print("y:", y)
print("z:", z)
