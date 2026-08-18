print("--- Recursion ---\n")

# --- Was ist Rekursion? ---
# Eine Funktion, die sich selbst aufruft – aber immer mit einer KLEINEREN Version
# des Problems. Das macht sie so lange, bis sie einen sogenannten "Basisfall"
# (Base Case) erreicht, der diese Kette stoppt.


def countdown(n):
    # Der Basisfall (Base Case) / Die Abbruchbedingung:
    # Ohne diesen Fall würde die Funktion endlos weiterlaufen.
    if n == 0:
        return

    # Die eigentliche Aktion in der aktuellen Ebene
    print(n)

    # Der rekursive Aufruf:
    # Die Funktion ruft sich selbst auf, aber mit n - 1.
    # Wir machen das Problem also bei jedem Schritt etwas kleiner.
    countdown(n - 1)


# countdown(3)


# --- Was ist ein Call Stack (Aufrufstapel)? ---

# Ein Call Stack ist ein Mechanismus des Interpreters, um den Überblick
# zu behalten: Welche Funktion wird gerade ausgeführt? Welche Funktion hat diese
# Funktion aufgerufen? Und wo muss ich am Ende eigentlich wieder zurückkehren?
# (Wie ein Stapel Notizzettel, den der Computer abarbeitet).

# Eigenschaften des Call Stacks:
# - Speichert: Jeden Funktionsaufruf, lokale Variablen und die Rücksprungadresse.
# - Automatisch verwaltet: Sobald eine Funktion fertig ist (return), wird ihr Speicherplatz sofort wieder freigegeben.
# - Begrenzte Größe: Der Stack-Speicher ist sehr klein (ca. 1–8 MB, je nach Betriebssystem).
# - Stack Overflow: Genau dieser Fehler passiert, wenn die Grenze überschritten wird
#   (z. B. wenn wir vergessen haben, einen Basisfall einzubauen und unendlich viele "Zettel" stapeln).


# --- Visualisierung des Call Stacks bei countdown(3) ---
# Jeder Einzug nach rechts bedeutet: Ein neuer "Zettel" wird auf den Stapel gelegt.
# Sobald 'return' erreicht wird, wird der Stapel von oben nach unten wieder abgebaut.

# countdown(3)
#   └── countdown(2)
#         └── countdown(1)
#               └── countdown(0)  ← Basisfall erreicht! Funktion stoppt und "returns" (Zettel wird entfernt)
#               ← kehrt zurück zu countdown(1), Funktion ist zu Ende (Zettel wird entfernt)
#         ← kehrt zurück zu countdown(2), Funktion ist zu Ende (Zettel wird entfernt)
#   ← kehrt zurück zu countdown(3), Programm ist komplett fertig!
