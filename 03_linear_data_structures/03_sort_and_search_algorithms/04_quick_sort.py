print("--- Quick Sort ---\n")

"""
Funktionsweise:

- Wähle ein Element als Pivot.
- Teile das Array in zwei Bereiche:
  - Elemente kleiner oder gleich dem Pivot → links
  - Elemente größer als das Pivot → rechts
- Sortiere beide Bereiche rekursiv.
- Füge linke Seite, Pivot und rechte Seite wieder zusammen.
- Der Basisfall ist erreicht, wenn das Array 0 oder 1 Element enthält.
"""

"""
Komplexität

| Fall    | Zeit       | Speicher |
| ------- | ---------- | -------- |
| Best    | O(n log n) | O(log n) |
| Average | O(n log n) | O(log n) |
| Worst   | O(n²)      | O(n)     |

Bester Fall (Best Case):
Das Pivot teilt das Array ungefähr in zwei gleich große Hälften.
Dadurch entstehen ungefähr log(n) Rekursionsebenen.
Auf jeder Ebene müssen insgesamt n Elemente betrachtet werden.
→ O(n log n)

Durchschnittlicher Fall (Average Case):
Bei einer einigermaßen ausgewogenen Pivot-Wahl ist die Laufzeit ebenfalls
O(n log n).

Schlechtester Fall (Worst Case):
Das Pivot ist immer das kleinste oder größte Element.
Dann wird das Array extrem unausgewogen geteilt:
[1, 2, 3, 4, 5]
→ [1, 2, 3, 4] + [5]
→ [1, 2, 3] + [4]
→ [1, 2] + [3]
→ [1] + [2]

Dadurch entstehen n Rekursionsebenen.
→ O(n²)

Speicher:
Die Rekursion benötigt Speicher auf dem Call Stack.
Bei einer ausgewogenen Aufteilung sind es O(log n) Ebenen.
Im schlechtesten Fall können es O(n) Ebenen sein.

Hinweis:
Diese Implementierung verwendet List Comprehensions und erstellt für
left und right neue Listen. Dadurch ist sie nicht vollständig "In-Place",
obwohl Quick Sort grundsätzlich In-Place implementiert wird.
"""

# unsorted_array = [10, 7, 8, 9, 1, 5]
# print("original:", unsorted_array)


# def fake_quick_sort(array):
#     if len(array) <= 1:
#         return array

#     pivot = array[-1]

#     left = [x for x in array[:-1] if x <= pivot]

#     right = [x for x in array[:-1] if x > pivot]

#     return fake_quick_sort(left) + [pivot] + fake_quick_sort(right)


# sorted_array = fake_quick_sort(unsorted_array)
# print("\nsorted:", sorted_array)

# --- Quick Sort (in-place) und mit einem zufälligen Pivot ---

import random

unsorted_array = [10, 7, 8, 9, 1, 5]
print("original:", unsorted_array)


import random


def partition(array, left, right):
    """Teilt das Array um ein Pivot-Element herum auf und gibt dessen finale Position zurück."""

    # Randomisiertes Pivot: Verhindert den Worst-Case O(n²) bei bereits (fast) sortierten Arrays
    pivot_index = random.randint(left, right)

    # Pivot ans Ende verschieben, um es für die folgende Schleife aus dem Weg zu räumen
    array[pivot_index], array[right] = array[right], array[pivot_index]
    pivot_value = array[right]

    # i markiert die rechte Grenze des Bereichs für Elemente, die kleiner/gleich dem Pivot sind
    i = left - 1

    # Durchsuche das Array bis zum vorletzten Element (das letzte ist unser Pivot)
    for j in range(left, right):
        if array[j] <= pivot_value:
            # Wenn ein kleineres Element gefunden wird: Erweitere den "kleineren" Bereich...
            i += 1
            # ...und tausche das gefundene Element (j) in diesen Bereich (i)
            array[i], array[j] = array[j], array[i]

    # Das Pivot an seine endgültige Position (zwischen kleinere und größere Elemente) setzen
    array[i + 1], array[right] = array[right], array[i + 1]

    return i + 1  # Gibt den finalen Index des Pivots zurück


def quick_sort(array, left, right):
    """Sortiert ein Array in-place aufsteigend mit Quick Sort (Divide & Conquer)."""

    # Basisfall: Wenn left >= right ist, hat das (Teil-)Array 1 oder 0 Elemente und ist fertig sortiert
    if left < right:
        # 1. Divide: Array aufteilen und die finale Position des Pivots erhalten
        pivot_index = partition(array, left, right)

        # 2. Conquer: Linken und rechten Teil rekursiv sortieren
        # Wichtig: Das Pivot selbst (pivot_index) wird exkludiert, da es bereits am richtigen Platz ist!
        quick_sort(array, left, pivot_index - 1)
        quick_sort(array, pivot_index + 1, right)

    return array


sorted_array = quick_sort(unsorted_array, 0, len(unsorted_array) - 1)
print("sorted:", sorted_array)
