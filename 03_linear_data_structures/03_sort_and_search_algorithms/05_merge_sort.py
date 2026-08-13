print("--- Merge Sort ---\n")

"""
Funktionsweise:

- Teile das Array immer wieder in zwei Hälften.
- Sortiere beide Hälften rekursiv.
- Füge die beiden bereits sortierten Hälften mit merge() zusammen.
- Der Basisfall ist erreicht, wenn das Array 0 oder 1 Element enthält.
- Merge Sort teilt immer ungefähr in der Mitte.
  Dadurch entsteht unabhängig von der Eingabe eine Laufzeit von O(n log n).
"""

"""
Komplexität

| Fall    | Zeit       | Speicher |
| ------- | ---------- | -------- |
| Best    | O(n log n) | O(n)     |
| Average | O(n log n) | O(n)     |
| Worst   | O(n log n) | O(n)     |

Bester Fall (Best Case):
Auch wenn das Array bereits sortiert ist, muss Merge Sort die Daten
weiterhin teilen und anschließend zusammenführen.
→ O(n log n)

Durchschnittlicher Fall (Average Case):
Das Array wird immer in Hälften geteilt und anschließend zusammengeführt.
→ O(n log n)

Schlechtester Fall (Worst Case):
Auch bei einer ungünstigen Eingabereihenfolge bleibt die Aufteilung
ausgeglichen.
Deshalb gibt es keinen O(n²)-Worst-Case wie bei Quick Sort.
→ O(n log n)

Speicher:
Beim Merging werden zusätzliche Listen erstellt.
Daher benötigt diese Implementierung O(n) zusätzlichen Speicher auf dem Heap.

Zusätzlich benötigt die Rekursion O(log n) Stack-Speicher.
Der dominante zusätzliche Speicherbedarf bleibt jedoch O(n).
"""

unsorted_array = [38, 27, 43, 3, 9, 82, 10]
print("original:", unsorted_array)


def merge(left, right):
    """Führt zwei bereits aufsteigend sortierte Arrays (left, right) zu einem zusammen."""
    result = []

    # Zeiger (Pointer) für das Durchlaufen der linken (i) und rechten (j) Hälfte
    i = 0
    j = 0

    # Vergleiche die Elemente beider Hälften, solange in BEIDEN noch Elemente vorhanden sind
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])  # Das kleinere Element kommt ins Ergebnis
            i += 1  # Zeiger der linken Hälfte weiterrücken
        else:
            result.append(right[j])
            j += 1

    # Restliche Elemente anhängen (es bleibt immer nur in genau EINER Hälfte ein Rest übrig)
    # Ist die Liste leer, wird einfach nichts angehängt.
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(array):
    """Sortiert ein Array aufsteigend mit Merge Sort (Divide & Conquer) out-of-place."""

    # Basisfall (Base Case): Ein Array der Länge 0 oder 1 ist per Definition bereits sortiert
    if len(array) <= 1:
        return array

    # 1. Divide: Finde die Mitte, um das Array in zwei Hälften zu spalten
    mid = len(array) // 2

    # 2. Conquer: Sortiere beide Hälften rekursiv
    # Hinweis: Durch das Slicing (array[:mid]) entstehen hier neue Listenkopien im Speicher
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    # 3. Combine: Füge die nun sortierten Hälften nach dem Reißverschlussprinzip zusammen
    return merge(left, right)
