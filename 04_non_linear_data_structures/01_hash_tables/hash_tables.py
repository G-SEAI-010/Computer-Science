# ==============================================================================
# ABSCHNITT 1: Das kennen wir bereits
# ==============================================================================

# # Das ist eine Hash Map — dieses Muster hast du schon mal benutzt
# student = {
#     "name": "Alice",
#     "avg": 91,
# }
# print(student["name"])  # O(1) Suchzugriff


# # Das ist ein Hash Set — auch dies kennen wir bereits
# subjects = {"Math", "English", "Science"}
# if "Math" in subjects:  # O(1) Überprüfung der Zugehörigkeit
#     print("enrolled in Math")

# ==============================================================================
# ABSCHNITT 2: Was sind Kollisionen?
# ==============================================================================

# Eine Kollision tritt auf, wenn zwei verschiedene Schlüssel denselben Hash-Index erzeugen
# Beispiel mit size=8:
#   hash("Alice") % 8 = 6
#   hash("Bob") % 8 = 3
#   hash("Dan") % 8 = 3  ← Kollision! Sowohl Bob als auch Dan wollen in Bucket 3

# Zwei Wege, um mit Kollisionen umzugehen:

# 1. CHAINING (Verkettung):
#    Jeder Bucket enthält eine Liste aller Elemente, deren Hash auf diesen Index verweist
#    Bucket 3: [('Bob', 85), ('Dan', 78)]
#    Suchen: Den Schlüssel hashen, zum Bucket gehen, die Liste durchsuchen

# 2. OPEN ADDRESSING (Offene Adressierung):
#    Wenn ein Bucket belegt ist, suche nach dem nächsten freien Platz
#    Versuche index, index+1, index+2, ... bis du einen leeren Platz findest

# Warum Kollisionen wichtig sind:
# - Bei Chaining: Wenn ein Bucket k Elemente hat, ist die Suche O(k)
# - Gute Hash-Funktion + niedriger Load Factor hält k klein (meistens 1-2)
# - Schlimmster Fall (Worst Case): alle Elemente in einem Bucket = O(n) Suche

# ==============================================================================
# ABSCHNITT 3: Den Load Factor verstehen
# ==============================================================================

# Load Factor = Anzahl der Elemente / Anzahl der Buckets

# Niedriger Load Factor (spärlich belegt)
# buckets = 10, elements = 3
# load factor = 3/10 = 0.3
# Buckets: [[], [element], [], [], [element], [], [], [element], [], []]
# Viel leerer Platz, wenige Kollisionen

# Hoher Load Factor (überfüllt)
# buckets = 10, elements = 15
# load factor = 15/10 = 1.5
# Buckets: [[element, element], [element], [element, element, element], [], [element], ...]
# Viele Kollisionen, langsamere Suchvorgänge

# Warum das wichtig ist:
# - Niedrig (< 0.5): Schnelle Suchen, verschwendet aber Speicherplatz
# - Mittel (0.5 - 0.75): Gute Balance — der Sweet Spot
# - Hoch (> 0.75): Zu viele Kollisionen, Leistung nimmt ab

# ==============================================================================
# ABSCHNITT 4: Hash Set Implementierung
# ==============================================================================


class HashSet:
    def __init__(self, size=8):
        """Initialisiert das Hash Set mit einer festen Anzahl an Buckets."""
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_func(self, key):
        """Eine einfache Hash-Funktion, die die Unicode-Werte der Zeichen summiert.
        Danach wird modulo self.size gerechnet, um einen Index zu erhalten."""
        if isinstance(key, str):
            return sum(ord(ch) for ch in key) % self.size
        if isinstance(key, int):
            return key % self.size
        return hash(key) % self.size

    def add(self, key):
        """Fügt einen Schlüssel in das Set ein, falls er nicht schon vorhanden ist."""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key):
        """Entfernt einen Schlüssel aus dem Set, falls er existiert."""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        try:
            bucket.remove(key)
        except ValueError:
            pass

    def __contains__(self, key):
        """Ermöglicht den 'in'-Operator: key in my_set"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        return key in bucket


print("------------------ HashSet ------------------\n")

my_set = HashSet()
my_set.add("Piano")
my_set.add("Running")
my_set.add("Piano")  # Duplikat — wird nicht zweimal eingefügt

print("Ist 'Piano' in my_set?", "Piano" in my_set)  # True
print("Ist 'Skiing' in my_set?", "Skiing" in my_set)  # False

my_set.remove("Piano")
my_set.remove("Piano")
print("Ist 'Piano' nach Löschung in my_set?", "Piano" in my_set)  # False

print()

# ==============================================================================
# ABSCHNITT 5: Beispiel für eine Hash-Kollision
# ==============================================================================

# Berechnungen unserer eigenen Hash-Funktion (mit size=8):
# "Alice" = (65+108+105+99+101) = 478 % 8 = 6
# "Bob" = (66+111+98) = 275 % 8 = 3
# "Dan" = (68+97+110) = 275 % 8 = 3 ← Kollision mit Bob!
# "Eve" = (69+118+101) = 288 % 8 = 0

# Daraus resultierende Bucket-Verteilung:
# Bucket 0: [('Eve', 95)]
# Bucket 1: []
# Bucket 2: []
# Bucket 3: [('Bob', 85), ('Dan', 78)] ← Hier gibt es eine Kollision!
# Bucket 4: []
# Bucket 5: []
# Bucket 6: [('Alice', 92)]
# Bucket 7: []

# ==============================================================================
# ABSCHNITT 6: Hash Map Implementierung
# ==============================================================================


class HashMap:
    def __init__(self, size=8):
        """Initialisiert die Hash Map mit einer festen Anzahl an Buckets."""
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_func(self, key):
        """Eine einfache Hash-Funktion, die die Unicode-Werte der Zeichen summiert.
        Danach wird modulo self.size gerechnet, um einen Index zu erhalten."""
        if isinstance(key, str):
            return sum(ord(ch) for ch in key) % self.size
        if isinstance(key, int):
            return key % self.size
        return hash(key) % self.size

    def __setitem__(self, key, value):
        """Ermöglicht die Zuweisung: my_map[key] = value"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Vorhandenen Schlüssel aktualisieren
                return
        bucket.append((key, value))

    def __getitem__(self, key):
        """Ermöglicht den Lesezugriff: my_map[key]"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(f"Schlüssel '{key}' nicht gefunden")

    def __delitem__(self, key):
        """Ermöglicht das Löschen: del my_map[key]"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(f"Schlüssel '{key}' nicht gefunden")

    def __contains__(self, key):
        """Ermöglicht den 'in'-Operator: key in my_map"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for k, _ in bucket:
            if k == key:
                return True
        return False

    def get(self, key, default=None):
        """Holt einen Wert mit optionalem Standardwert (wie dict.get())"""
        try:
            return self[key]
        except KeyError:
            return default


print("------------------ HashMap ------------------\n")

my_map = HashMap()
my_map["Book"] = 12.99
my_map["Laptop"] = 999.00
my_map["Book"] = 10.99  # Wert aktualisieren

print("Buch Preis:", my_map["Book"])  # 10.99
print("Laptop Preis:", my_map["Laptop"])  # 999.00
print("Ist 'Phone' in my_map?", "Phone" in my_map)  # False
print("Ist 'Book' in my_map?", "Book" in my_map)  # True
print("Telefon Preis:", my_map.get("Phone", 0))  # 0 (Standardwert)

del my_map["Book"]
print("Buch Preis nach Löschung:", my_map.get("Book"))  # None
