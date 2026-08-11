print("--- Insertion Sort ---\n")

"""
Funktionsweise:
- Baue einen sortierten Bereich von links nach rechts auf, ein Element nach dem anderen
- Nimm das nächste unsortierte Element und verschiebe größere Elemente nach rechts, um Platz zu machen
- Füge das Element an seiner korrekten Position im sortierten Bereich ein
- Bester Fall O(n) — wenn bereits sortiert, bleibt jedes Element einfach an seinem Platz
"""

"""
Komplexität
| Fall    | Zeit | Speicher |
|---------|------|----------|
| Best    | O(n) | O(1)     |
| Average | O(n²)| O(1)     |
| Worst   | O(n²)| O(1)     |

Bester Fall (Best Case): Array ist bereits sortiert — jedes Element ist bereits an seinem Platz, keine Verschiebungen nötig
Schlechtester Fall (Worst Case): Array ist umgekehrt sortiert — jedes Element muss den ganzen Weg nach vorne verschoben werden
"""

unsorted_array = [5, 1, 4, 2, 8]
print("original:", unsorted_array)


def insertion_sort(array):
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        while j >= 0 and array[j] > current:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current
    return array


sorted_array = insertion_sort(unsorted_array)
print("\nsorted:", sorted_array)

"""
Durchlauf 1 (Pass 1)
i = 1 | current = 1 | j startet bei 0
Vergleiche current (1) mit arr[j] (5) → 5 ist größer, verschiebe 5 nach rechts. j wird -1.
Stopp, da j < 0 ist.
Füge 1 an Index j + 1 (also -1 + 1 = Index 0) ein.
(Zustand: [1, 5, 4, 2, 8])

Durchlauf 2 (Pass 2)
i = 2 | current = 4 | j startet bei 1
Vergleiche current (4) mit arr[j] (5) → 5 ist größer, verschiebe 5 nach rechts. j wird 0.
Vergleiche current (4) mit arr[j] (1) → 1 ist kleiner, Stopp.
Füge 4 an Index j + 1 (also 0 + 1 = Index 1) ein.
(Zustand: [1, 4, 5, 2, 8])

Durchlauf 3 (Pass 3)
i = 3 | current = 2 | j startet bei 2
Vergleiche current (2) mit arr[j] (5) → 5 ist größer, verschiebe 5 nach rechts. j wird 1.
Vergleiche current (2) mit arr[j] (4) → 4 ist größer, verschiebe 4 nach rechts. j wird 0.
Vergleiche current (2) mit arr[j] (1) → 1 ist kleiner, Stopp.
Füge 2 an Index j + 1 (also 0 + 1 = Index 1) ein.
(Zustand: [1, 2, 4, 5, 8])

Durchlauf 4 (Pass 4)
i = 4 | current = 8 | j startet bei 3
Vergleiche current (8) mit arr[j] (5) → 5 ist kleiner, Stopp.
Füge 8 an Index j + 1 (also 3 + 1 = Index 4) ein (bleibt an ihrer Position).
(Zustand: [1, 2, 4, 5, 8])
"""
