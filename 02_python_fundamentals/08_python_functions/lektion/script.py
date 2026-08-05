print("--- Einfache Funktion ---\n")


# Die simpelste Funktion — keine Argumente, kein Rückgabewert
def say_hello():
    print("Hallo!")


say_hello()  # Aufruf der Funktion


# Eine Funktion ohne return-Anweisung gibt implizit None zurück
def do_nothing():
    pass


result = do_nothing()
print("Ergebnis:", result)  # None

print("\n--- Argumente und Rückgabe (return) ---\n")


# Positionsargumente — die Reihenfolge ist wichtig
def greet(name, greeting):
    return f"{greeting}, {name}!"


print(greet("Alice", "Hallo"))  # nach Position: erst name, dann greeting
print(greet("Hallo", "Alice"))  # vertauscht — falsches Ergebnis, aber kein Fehler

print()


# Standardparameter — werden verwendet, wenn kein Argument übergeben wird
def greet_default(name, greeting="Hallo"):
    return f"{greeting}, {name}!"


print(greet_default("Bob"))  # nutzt die Standard-Begrüßung
print(greet_default("Bob", "Hey"))  # überschreibt den Standardwert

# Schlüsselwort-Argumente — nach Namen übergeben, Reihenfolge ist egal
print(greet_default(greeting="Hi", name="Charlie"))

print()


# Unterschied zwischen Rückgabe (return) und keiner Rückgabe
def add_with_return(a, b):
    return a + b  # sendet das Ergebnis an den Aufrufer zurück


def add_no_return(a, b):
    result = a + b  # berechnet es, sendet es aber nie zurück
    # keine return-Anweisung


print("Mit Rückgabe:", add_with_return(3, 4))  # 7
print("Ohne Rückgabe:", add_no_return(3, 4))  # None

print()


# Mehrere Werte zurückgeben — Python packt sie in ein Tupel
def min_max(numbers):
    return min(numbers), max(numbers)


low, high = min_max([3, 1, 9, 4, 7])  # das Tupel entpacken (Unpacking)
print("Minimum:", low)
print("Maximum:", high)

print("\n--- *args und **kwargs ---\n")


# *args — sammelt eine beliebige Anzahl von Positionsargumenten in einem Tupel
# nützlich, wenn man nicht weiß, wie viele Werte übergeben werden
def total(*numbers):
    # numbers ist ein Tupel: (1, 2, 3, 4, 5)
    print("Erhalten:", numbers)
    return sum(numbers)


print("Gesamt:", total(1, 2, 3))
print("Gesamt:", total(1, 2, 3, 4, 5, 6))

print()


# **kwargs — sammelt eine beliebige Anzahl von Schlüsselwort-Argumenten in einem Dictionary
# nützlich für flexible Konfigurationen oder benannte Optionen
def describe(**info):
    # info ist ein Dict: {"name": "Alice", "age": 25, ...}
    for key, value in info.items():
        print(f"  {key}: {value}")


describe(name="Alice", age=25, city="Berlin")

print()


# Beides kombinieren — *args muss vor **kwargs stehen
def mixed(required, *args, **kwargs):
    print("Erforderlich:", required)
    print("Zusätzliche positionelle:", args)
    print("Zusätzliche Schlüsselwörter:", kwargs)


mixed("hallo", 1, 2, 3, 4, color="rot", size="groß")

print("\n--- Lambda ---\n")

# lambda ist eine anonyme Einzeiler-Funktion
# Syntax: lambda parameter: ausdruck

# Einfache Lambda-Funktion, die einer Variablen zugewiesen wird
square = lambda x: x**2
print("Quadrat von 5:", square(5))

# Lambda mit mehreren Parametern
add = lambda a, b: a + b
print("Addiere 3 + 4:", add(3, 4))

print()

# Lambda innerhalb einer Funktion — häufiger Anwendungsfall
# sorted() und map() akzeptieren eine Funktion als Argument
students = [
    {"name": "Charlie", "avg": 95},
    {"name": "Alice", "avg": 88},
    {"name": "Bob", "avg": 72},
]

# Nach Durchschnitt sortieren — Lambda definiert, wonach sortiert wird
sorted_students = sorted(students, key=lambda student: student["avg"], reverse=True)
print(sorted_students)

# for student in sorted_students:
#     print(f"  {student['name']}: {student['avg']}")

print()

# map — wendet eine Funktion auf jedes Element in einem iterierbaren Objekt
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda number: number**2, numbers))
print("Quadriert:", squared)

print()

# filter — behält nur die Elemente, bei denen die Funktion True zurückgibt
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Gerade Zahlen:", evens)

print("\n--- Gültigkeitsbereich (Scope) ---\n")


# Variablen innerhalb einer Funktion sind lokal (Funktions-Scope) — von außen unsichtbar
def my_function():
    local_var = "Mich gibt es nur hier drinnen"
    print("Innerhalb der Funktion:", local_var)


my_function()
# print(local_var)  # NameError — existiert hier draußen nicht

print()

# global — eine Variable verändern, die außerhalb der Funktion lebt
counter = 0


def increment():
    global counter
    counter += 1


increment()
increment()
print("Zähler:", counter)

print("\n--- Fehlerbehandlung (Error Handling) ---\n")

# try: Code, der fehlschlagen könnte
# except: wird ausgeführt, wenn ein Fehler auftritt
# else: wird NUR ausgeführt, wenn KEIN Fehler aufgetreten ist
# finally: wird immer ausgeführt, egal ob Fehler oder nicht


def divide(a, b):
    try:
        result = round(a / b, 2)
    except ZeroDivisionError:
        print("Fehler: Teilen durch null nicht möglich")
        return None
    else:
        print("Erfolg: Keine Fehler aufgetreten")
        return result  # wird nur erreicht, wenn es keine Exception gab
    finally:
        print("finally: Das hier wird immer ausgeführt")


print("10 / 2 =", divide(10, 3))
print()
print("10 / 0 =", divide(10, 0))

print()


# Mehrere Exception-Typen (Fehlerarten) abfangen
def parse_input(value):
    try:
        number = int(value)
        result = 100 / number
    except ValueError:
        print("Fehler: Keine gültige Zahl")
        return None
    except ZeroDivisionError:
        print("Fehler: Teilen durch null nicht möglich")
        return None
    except Exception as My_Error:
        print("Unerwarteter Fehler:", My_Error)  # Sammelbecken für alle anderen Fehler
        return None
    else:
        return result


print("parse '5':", parse_input("5"))
print()
print("parse 'abc':", parse_input("abc"))
print()
print("parse '0':", parse_input("0"))
