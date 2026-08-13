print("--- Bubble Sort ---\n")

"""
Funktionsweise:
- Vergleiche benachbarte Elemente, tausche sie, wenn sie in der falschen Reihenfolge sind
- Jeder vollständige Durchlauf verschiebt das größte unsortierte Element an seine endgültige Position
- Der sortierte Bereich wächst von rechts — daher schrumpft die innere Schleife mit jedem Durchlauf
- Vorzeitiger Abbruch (Early Exit): Wenn in einem Durchlauf keine Vertauschungen stattgefunden haben, ist das Array bereits sortiert → O(n) im besten Fall
"""

"""
Komplexität
| Fall    | Zeit | Speicher |
|---------|------|----------|
| Best    | O(n) | O(1)     |
| Average | O(n²)| O(1)     |
| Worst   | O(n²)| O(1)     |

Bester Fall (Best Case): Das Array ist bereits sortiert — der vorzeitige Abbruch greift nach einem Durchlauf ohne Vertauschungen.
Schlechtester Fall (Worst Case): Das Array ist komplett umgekehrt sortiert — jedes Element muss den ganzen Weg bis ans Ende "blubbern".
"""

unsorted_array = [5, 1, 4, 2, 8]
print("original:", unsorted_array)


def bubble_sort(array):
    """Sortiert ein Array in-place aufsteigend mit Bubble Sort."""
    n = len(array)

    for i in range(n):
        swapped = False  # Optimierung: Prüft, ob im aktuellen Durchlauf getauscht wurde

        # Innere Schleife: n-i-1, da die letzten i Elemente bereits fertig sortiert am Ende stehen
        for j in range(0, n - i - 1):

            # Benachbarte Elemente vergleichen
            if array[j] > array[j + 1]:
                # Pythonic Way: Direkter Tausch ohne temporäre Hilfsvariable
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        # Early Exit: Kein Tausch im gesamten Durchlauf bedeutet, das Array ist sortiert
        if not swapped:
            break

    return array


sorted_array = bubble_sort(unsorted_array)
print("\nsorted:", sorted_array)

"""
Durchlauf 1 (Pass 1)

i = 0 | Anzahl der Vergleiche: 5 - 0 - 1 = 4

Vergleich 1 (j = 0): Vergleiche Index 0 und 1 (5 und 1) → Tausch!
(Zustand: [1, 5, 4, 2, 8])
Vergleich 2 (j = 1): Vergleiche Index 1 und 2 (5 und 4) → Tausch!
(Zustand: [1, 4, 5, 2, 8])
Vergleich 3 (j = 2): Vergleiche Index 2 und 3 (5 und 2) → Tausch!
(Zustand: [1, 4, 2, 5, 8])
Vergleich 4 (j = 3): Vergleiche Index 3 und 4 (5 und 8) → Kein Tausch.
(Zustand: [1, 4, 2, 5, 8])


Durchlauf 2 (Pass 2)

i = 1 | Anzahl der Vergleiche: 5 - 1 - 1 = 3

Vergleich 1 (j = 0): Vergleiche Index 0 und 1 (1 und 4) → Kein Tausch.
(Zustand: [1, 4, 2, 5, 8])
Vergleich 2 (j = 1): Vergleiche Index 1 und 2 (4 und 2) → Tausch!
(Zustand: [1, 2, 4, 5, 8])
Vergleich 3 (j = 2): Vergleiche Index 2 und 3 (4 und 5) → Kein Tausch.
(Zustand: [1, 2, 4, 5, 8])


Durchlauf 3 (Pass 3)

i = 2 | Anzahl der Vergleiche: 5 - 2 - 1 = 2

Vergleich 1 (j = 0): Vergleiche Index 0 und 1 (1 und 2) → Kein Tausch.
(Zustand: [1, 2, 4, 5, 8])
Vergleich 2 (j = 1): Vergleiche Index 1 und 2 (2 und 4) → Kein Tausch.
(Zustand: [1, 2, 4, 5, 8])
"""
