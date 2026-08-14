print("--- Counting Sort ---\n")

"""
Funktionsweise:
- Zähle, wie oft jeder Wert vorkommt (keine Vergleiche nötig)
- Rekonstruiere das sortierte Array direkt aus den Zählungen
- Funktioniert mit nicht-negativen und negativen Ganzzahlen (Integers) innerhalb eines bekannten Bereichs
- Zwei Versionen: einfach (schnell zu verstehen) und stabil (erforderlich für Radix Sort)
"""

"""
Komplexität
| Fall    | Zeit     | Speicher |
|---------|----------|----------|
| Best    | O(n + k) | O(n + k) |
| Average | O(n + k) | O(n + k) |
| Worst   | O(n + k) | O(n + k) |

n = Anzahl der Elemente, k = Wertebereich (max - min)

Alle Fälle sind identisch: Zählt immer jedes Element und durchläuft den gesamten Bereich.
Am besten, wenn k im Verhältnis zu n klein ist — z. B. beim Sortieren von 10.000 Prüfungsergebnissen mit einem Bereich von 0-100.
Am schlechtesten, wenn k im Verhältnis zu n groß ist — z. B. erstellt [1, 2, 1000000] ein Count-Array mit einer Million Plätzen für nur 3 Werte.
"""

# ────────────────────────────────────────────
# Einfache Version (keine Stabilitätsgarantie)
# ────────────────────────────────────────────

# unsorted_array = [4, 2, 2, 8, 3, 3, 1]
# print("original:", unsorted_array)


# def counting_sort_simple(array):
#     # max und min finden, um den Bereich (k) zu bestimmen
#     max_val = max(array)
#     min_val = min(array)
#     k = max_val - min_val + 1

#     # Count-Array erstellen, das exakt der Größe des Bereichs (k) entspricht
#     count = [0] * k

#     # Jeden Wert zählen (min_val abziehen, um den Index zu verschieben)
#     for number in array:
#         count[number - min_val] += 1

#     """
#     Index(i)  Häuf.   [i + min_val] * freq     Bedeutung
#     0         1       [1]                      Wert 1 kam 1-mal vor
#     1         2       [2, 2]                   Wert 2 kam 2-mal vor
#     2         2       [3, 3]                   Wert 3 kam 2-mal vor
#     3         1       [4]                      Wert 4 kam 1-mal vor
#     4-6       0       []                       Werte 5-7 kamen 0-mal vor
#     7         1       [8]                      Wert 8 kam 1-mal vor
#     """

#     result = []

#     # Rekonstruieren, min_val wieder zu "i" addieren, um die ursprüngliche Zahl wiederherzustellen
#     for i, freq in enumerate(count):
#         result.extend([i + min_val] * freq)

#     return result


# sorted_array = counting_sort_simple(unsorted_array)
# print("\nsorted:", sorted_array)

# ─────────────────────────────────────────────
# Stabile Version (erforderlich für Radix Sort)
# ─────────────────────────────────────────────

unsorted_array = [4, 2, 2, 8, 3, 3, 1]
print("original:", unsorted_array)


def counting_sort_stable(array):
    max_val = max(array)
    min_val = min(array)
    k = max_val - min_val + 1

    count = [0] * k
    print("\ncount nach Initialisierung:", count)

    for number in array:
        count[number - min_val] += 1
    print("count nach Zählung:", count)

    # Kumulative Summe - jede Position hält den letzten Index für diesen Wert
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    print("count kumulativ:", count)

    # Elemente in das Ergebnis einfügen, rückwärts durchlaufen für Stabilität
    result = [0] * len(array)

    for number in reversed(array):
        # Offset anwenden, um den richtigen Index im Count-Array zu finden
        count_index = number - min_val

        # Um 1 verringern, um einen 0-basierten Index zu erhalten
        count[count_index] -= 1

        # An der korrekten Position einfügen
        result[count[count_index]] = number

    return result


"""
Ablauf mit min_val Offset verfolgen (aktueller Wert - 1 = count_index):

current = 1  → count_idx=0 → cumulative[0]=1 (verringert auf 0) → result: [1, _, _, _, _, _, _]
current = 3  → count_idx=2 → cumulative[2]=5 (verringert auf 4) → result: [1, _, _, _, 3, _, _]
current = 3  → count_idx=2 → cumulative[2]=4 (verringert auf 3) → result: [1, _, _, 3, 3, _, _]
current = 8  → count_idx=7 → cumulative[7]=7 (verringert auf 6) → result: [1, _, _, 3, 3, _, 8]
current = 2  → count_idx=1 → cumulative[1]=3 (verringert auf 2) → result: [1, _, 2, 3, 3, _, 8]
current = 2  → count_idx=1 → cumulative[1]=2 (verringert auf 1) → result: [1, 2, 2, 3, 3, _, 8]
current = 4  → count_idx=3 → cumulative[3]=6 (verringert auf 5) → result: [1, 2, 2, 3, 3, 4, 8]
"""


sorted_array = counting_sort_stable(unsorted_array)
print("\nsorted:", sorted_array)
