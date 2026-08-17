print("--- Linear Search ---\n")

"""
Funktionsweise:
- Prüft jedes Element nacheinander von links nach rechts.
- Gibt den Index zurück, sobald der gesuchte Wert (Target) gefunden wurde.
- Gibt -1 zurück, wenn der Wert nicht im Array existiert.
- Funktioniert mit allen Daten — egal ob sortiert oder unsortiert.
"""

"""
Komplexität:
| Fall          | Zeit | Speicher |
|---------------|------|----------|
| Best          | O(1) | O(1)     |
| Average       | O(n) | O(1)     |
| Worst         | O(n) | O(1)     |

Bester Fall (Best Case): Der gesuchte Wert ist direkt das erste Element.
Schlechtester Fall (Worst Case): Der gesuchte Wert ist das letzte Element oder gar nicht im Array.
"""

numbers = [4, 2, 7, 1, 8, 10, 5, 22, 1]


def linear_search(array, target):
    """Sucht nach 'target' in 'array' und gibt den ersten gefundenen Index zurück."""

    # 'enumerate' ist der pythonische Weg, um gleichzeitig den Index (i)
    # und das eigentliche Element (value) in einer Schleife zu erhalten
    for i, value in enumerate(array):
        if value == target:
            return i  # Gefunden — den Index sofort zurückgeben (Early Exit)

    return -1  # Die gesamte Schleife wurde durchlaufen, ohne den Wert zu finden


index = linear_search(numbers, 100)
if index != -1:
    print("Zahl gefunden an Index:", index)
else:
    print("Zahl nicht gefunden.")


# --- Variante: Finde alle Vorkommen eines Wertes ---

numbers_duplicates = [1, 1, 10, 20, 5, 6, 3, 1]


def linear_search_all(array, target):
    """Sucht nach allen Vorkommen von 'target' und gibt eine Liste der Indizes zurück."""

    return [i for i, value in enumerate(array) if value == target]


print("\nAlle Index-Positionen der Zahl 1:", linear_search_all(numbers_duplicates, 1))
