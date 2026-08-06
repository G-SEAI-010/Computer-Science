print("\n--- Grundlegende Klassen-Syntax ---\n")


class House:
    def __init__(self, color, num_rooms):
        self.color = color  # Instanz-Attribut: Spezifisch für dieses Objekt
        self.num_rooms = num_rooms  # Instanz-Attribut

    def open_door(self):
        print("\nDie Tür öffnet sich")

    # Klassen-Attribut (Class Attribute): Gilt für ALLE Instanzen dieser Klasse
    building_type = "Residential"


# Erstellen von zwei unabhängigen Objekten aus demselben Bauplan
house_1 = House("weiß", 3)
house_2 = House("rot", 5)

house_1.building_type = "Commercial"

print("house_1 Farbe:", house_1.color)
print("house_2 Zimmer:", house_2.num_rooms)

# Beide greifen auf dasselbe Klassen-Attribut zu
print("\nhouse_1 Typ:", house_1.building_type)
print("house_2 Typ:", house_2.building_type)

house_1.open_door()


print("\n--- __str__ und Methoden ---\n")


class House:
    def __init__(self, color, num_rooms):
        self.color = color
        self.num_rooms = num_rooms
        self.is_locked = True

    def __str__(self):
        status = "verschlossen" if self.is_locked else "offen"
        return f"Das Haus ist {self.color} und hat {self.num_rooms} Zimmer und ist momentan {status}"

    def open_door(self):
        print("\nDie Tür öffnet sich")

    def lock(self):
        self.is_locked = True
        print("Haus abgeschlossen")

    def unlock(self):
        self.is_locked = False
        print("Haus aufgeschlossen")


house_3 = House("blau", 4)  # nutzt __init__
print("Haus:", house_3)  # nutzt __str__

house_3.unlock()
print("Haus:", house_3)

print("\n--- Mehrere Instanzen ---\n")


class House:
    def __init__(self, color, num_rooms):
        self.color = color
        self.num_rooms = num_rooms

    def describe(self):
        print("Farbe:", self.color)
        print("Zimmer:", self.num_rooms)

    def repaint(self, new_color):
        self.color = new_color
        print("Neu gestrichen zu:", self.color)

    def __str__(self):
        return f"{self.color} Haus ({self.num_rooms} Zimmer)"


house_4 = House("weiß", 3)
house_5 = House("rot", 5)

# Jede Instanz hat ihre eigenen Daten
house_4.describe()
print()
house_5.describe()

print()

# Das Ändern einer Instanz hat keine Auswirkungen auf die andere
house_4.repaint("gelb")
print("house_4:", house_4)
print("house_5:", house_5)

print("\n--- Kapselung ---\n")


class Safe:
    def __init__(self, password):
        # Der Unterstrich signalisiert: Dieses Attribut ist "privat" (intern)
        self._password = password
        self._is_open = False

    def unlock(self, attempt):
        if attempt == self._password:
            self._is_open = True
            print("Safe entsperrt!")
        else:
            print("Falsches Passwort!")


my_safe = Safe("1234")

# Wir interagieren mit dem Objekt NUR über seine Methoden
my_safe.unlock("1234")

# Direkter Zugriff auf "private" Attribute (sollte vermieden werden!)
my_safe._is_open = True
