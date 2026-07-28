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

print("\n--- Typumwandlung (Type Casting) ---\n")

# Konvertieren zwischen Typen
age = 25
age_str = str(age)
print("age im String-Format:", "Ich bin " + age_str + " Jahre alt!")

# Umwandlungsbeispiele
float_example = float(5)
bool_example = bool(1)

print("float(5):", float_example)
print("bool(1):", bool_example)

# Vorsicht bei ungültigen Umwandlungen!
# invalid = int("hello")

print("\n--- Arithmetik ---\n")

# Arithmetische Operationen
a = 11
b = 3

print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)
print("a / b:", a / b)
print("a // b:", a // b)
print("a ** b:", a**b)
print("a % b:", a % b)

# Typen mischen
result = 5 + 2.5
print("5 + 2.5:", result, type(result))

print("\n--- String-Grundlagen ---\n")

# Strings erstellen
single_quotes = "Hello"
double_quotes = "World"
multi_line = """This is a
multi-line
string"""

# String-Verkettung (Concatenation)
greeting = "Hello" + " " + "Python"
print("greeting:", greeting)

# String-Wiederholung
laugh = "ha" * 3
print("laugh:", laugh)

print("\n--- String-Methoden ---\n")

text = "  Hello Python World  "

# Groß-/Kleinschreibung umwandeln
print("upper:", text.upper())
print("lower:", text.lower())
print("title:", text.title())

# Leerzeichen entfernen
print("strip:", text.strip())
print("lstrip:", text.lstrip())
print("rstrip:", text.rstrip())

# Ersetzen
print("replace:", text.replace("Python", "Java"))

# Inhalt prüfen
print("'Python' in text:", "Python" in text)
print("'Java' not in text:", "Java" not in text)

print("\n--- String-Formatierung ---\n")

name = "Alice"
age = 25

# f-strings (Python 3.6+) - EMPFOHLEN
message1 = f"Mein Name ist {name} und ich bin {age} Jahre alt."
print("f-string:", message1)

# Formatierung mit Ausdrücken
message2 = f"In 5 Jahren werde ich {age + 5} Jahre alt sein."
print("expression:", message2)

print("\n--- Booleans und Truthy/Falsy-Werte ---\n")

# Boolean Werte
is_sunny = True
is_raining = False

print("is_sunny:", is_sunny)
print("is_raining:", is_raining)

# Truthy Werte (werden als True ausgewertet)
print("bool('Hello'):", bool("Hello"))
print("bool(42):", bool(42))

# Falsy Werte (werden als False ausgewertet)
print("bool(''):", bool(""))
print("bool(0):", bool(0))
print("bool(None):", bool(None))

# Verwendung von Booleans in Bedingungen
temperature = 25

is_warm = temperature > 20
print("is warm:", is_warm)

print("\n--- Vergleichsoperatoren ---\n")

x = 10
y = 5

print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= 10:", x >= 10)
print("y <= 5:", y <= 5)

# Strings vergleichen
print("'apple' < 'banana':", "apple" < "banana")
print("'Python' == 'python':", "Python" == "python")

print("\n--- Logische Operatoren ---\n")

# Logisches UND (and) - beide müssen True sein
age = 25
has_license = True
can_drive = age >= 18 and has_license
print("can drive:", can_drive)

# Logisches ODER (or) - mindestens eines muss True sein
is_weekend = False
is_holiday = True
can_relax = is_weekend or is_holiday
print("can relax:", can_relax)

# Logisches NICHT (not) - kehrt den Boolean um
is_raining = False
is_sunny = not is_raining
print("is sunny:", is_sunny)

# Logische Operatoren kombinieren
temperature = 25
is_summer = True
go_swimming = temperature > 20 and is_summer and not is_raining
print("go swimming:", go_swimming)

print("\n--- Zuweisungsoperatoren ---\n")

x = 10

x += 5
print("Nach +=5:", x)

x -= 3
print("Nach -=3:", x)

x *= 2
print("Nach *=2:", x)

x /= 4
print("Nach /=4:", x)

x //= 2
print("Nach //=2:", x)

x %= 2
print("Nach %=2:", x)

x = 2
x **= 3
print("Nach **=3:", x)
