print("--- Binary Search ---\n")

"""
Funktionsweise:
- Vergleicht den gesuchten Wert (Target) mit dem mittleren Element.
- Wenn das Target kleiner ist -> rechte Hälfte verwerfen, in der linken suchen.
- Wenn das Target größer ist -> linke Hälfte verwerfen, in der rechten suchen.
- Wiederholen, bis der Wert gefunden wurde oder der Suchbereich leer ist.
- VORAUSSETZUNG: Das Array MUSS aufsteigend sortiert sein!
"""

"""
Komplexität:
| Fall          | Zeit      | Speicher |
|---------------|-----------|----------|
| Best          | O(1)      | O(1)     |
| Average       | O(log n)  | O(1)     |
| Worst         | O(log n)  | O(1)     |

Bester Fall: Das Target ist genau das mittlere Element beim allerersten Check.
Schlechtester Fall: Das Target ist nicht im Array — der Suchbereich halbiert sich bis auf 0.
Warum log n? Jeder Schritt schließt die Hälfte der verbleibenden Elemente aus.
"""

sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 20]


def binary_search(array, target):
    """Sucht nach 'target' in einem SORTIERTEN Array 'array' und gibt den Index zurück."""

    # Startwerte der Zeiger: umfassen initial das gesamte Array
    left, right = 0, len(array) - 1

    # Wichtig: '<=' (nicht '<'), damit auch Teilbereiche der Länge 1 geprüft werden
    while left <= right:

        # Ganzzahldivision ('//'), da Index-Positionen keine Kommazahlen sein dürfen
        mid = (left + right) // 2

        if array[mid] == target:
            return mid  # Treffer — Index direkt zurückgeben
        elif array[mid] < target:
            # Das mittlere Element ist kleiner als unser Ziel.
            # Daher muss das Ziel in der rechten Hälfte liegen (+1, da 'mid' schon geprüft wurde)
            left = mid + 1
        else:
            # Das mittlere Element ist größer als unser Ziel.
            # Daher muss das Ziel in der linken Hälfte liegen (-1, aus demselben Grund)
            right = mid - 1

    return -1  # Schleife beendet, ohne den Wert zu finden -> nicht im Array


index = binary_search(sorted_numbers, 11)
if index != -1:
    print("Zahl gefunden an Index:", index)
else:
    print("Zahl nicht gefunden.")
