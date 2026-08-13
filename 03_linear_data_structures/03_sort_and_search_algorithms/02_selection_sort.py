print("--- Selection Sort ---\n")

"""
Funktionsweise:
- Finde das kleinste Element im unsortierten Teil, tausche es ganz nach vorne
- Jeder Durchlauf platziert ein Element an seiner endgültigen Position (das Minimum)
- Der sortierte Bereich wächst von links
- Kein vorzeitiger Abbruch (Early Exit) — durchsucht immer den kompletten unsortierten Teil, unabhängig von der Eingabe
"""

"""
Komplexität
| Fall    | Zeit | Speicher |
|---------|------|----------|
| Best    | O(n²)| O(1)     |
| Average | O(n²)| O(1)     |
| Worst   | O(n²)| O(1)     |

Bester Fall (Best Case): immer noch O(n²) — kein vorzeitiger Abbruch, durchsucht immer den kompletten unsortierten Teil
Schlechtester Fall (Worst Case): gleich — die Leistung ändert sich nie, unabhängig von der Eingabereihenfolge
"""

unsorted_array = [5, 1, 4, 2, 8]
print("original:", unsorted_array)


def selection_sort(array):
    """Sortiert ein Array in-place aufsteigend mit Selection Sort."""
    n = len(array)

    # i verschiebt schrittweise die Grenze zwischen dem sortierten (links)
    # und dem unsortierten Teil (rechts)
    for i in range(n):
        min_index = i  # Annahme: Das erste unsortierte Element ist das kleinste

        # Durchsuche ausschließlich den restlichen unsortierten Bereich (ab i + 1)
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j  # Neues Minimum gefunden -> Index merken

        # Optimierung: Nur tauschen, wenn das Minimum nicht ohnehin schon
        # an der richtigen Position (i) steht
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]

    return array


sorted_array = selection_sort(unsorted_array)
print("\nsorted:", sorted_array)

"""
Durchlauf 1 (Pass 1)
i = 0 | Suche Minimum ab Index 0
Vergleiche 5 mit 1, 4, 2, 8 → Minimum ist 1 (auf Index 1).
Tausche Index 0 (5) mit Index 1 (1).
(Zustand: [1, 5, 4, 2, 8])

Durchlauf 2 (Pass 2)
i = 1 | Suche Minimum ab Index 1
Vergleiche 5 mit 4, 2, 8 → Minimum ist 2 (auf Index 3).
Tausche Index 1 (5) mit Index 3 (2).
(Zustand: [1, 2, 4, 5, 8])

Durchlauf 3 (Pass 3)
i = 2 | Suche Minimum ab Index 2
Vergleiche 4 mit 5, 8 → Minimum ist 4 (auf Index 2).
Kein Tausch nötig, da 4 bereits an der richtigen Stelle steht.
(Zustand: [1, 2, 4, 5, 8])

Durchlauf 4 (Pass 4)
i = 3 | Suche Minimum ab Index 3
Vergleiche 5 mit 8 → Minimum ist 5 (auf Index 3).
Kein Tausch nötig.
(Zustand: [1, 2, 4, 5, 8])
"""
