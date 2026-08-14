print("--- Radix Sort ---\n")

"""
Funktionsweise:
- Sortiere Ziffer für Ziffer, von der niedrigstwertigen (Einer) zur höchstwertigen (Hunderter)
- Verwendet bei jedem Zifferndurchlauf einen stabilen Counting Sort
- Nach allen Durchläufen ist das Array vollständig sortiert
- Funktioniert (in dieser Standardimplementierung) nur mit nicht-negativen Ganzzahlen
- Keine Vergleiche — verwendet die Ziffernposition als Eimer-Index (Bucket-Index)
"""

"""
Komplexität
| Fall    | Zeit     | Speicher |
|---------|----------|----------|
| Best    | O(n × d) | O(n + k) |
| Average | O(n × d) | O(n + k) |
| Worst   | O(n × d) | O(n + k) |

n = Anzahl der Elemente, d = Anzahl der Ziffern im Maximalwert, k = Basis (10)

Alle Fälle sind identisch: Verarbeitet immer jede Ziffer jedes Elements.
Am besten, wenn d klein ist — z. B. beim Sortieren von Telefonnummern (alle gleich lang) oder Postleitzahlen.
Am schlechtesten, wenn d im Verhältnis zu n groß ist — z. B. beim Sortieren von 5 Zahlen, von denen eine 20 Ziffern hat.
"""

"""
digit = (num // exp) % 10  — extrahiert jeweils eine Ziffer:
  170 // 1   = 170 → 170 % 10 = 0   (Einerstelle)
  170 // 10  = 17  →  17 % 10 = 7   (Zehnerstelle)
  170 // 100 = 1   →   1 % 10 = 1   (Hunderterstelle)
"""

unsorted_array = [170, 45, 75, 90, 802, 24, 2, 66]
print("original:", unsorted_array)


def radix_sort(array, exp):
    n = len(array)
    output = [0] * n
    count = [0] * 10  # 10 Eimer (Buckets) für die Ziffern 0 - 9

    # Vorkommen jeder Ziffer an der Position exp zählen
    for number in array:
        digit = (number // exp) % 10  # Ziffer an dieser Position extrahieren
        count[digit] += 1

    # Kumulative Summe, notwendig für die stabile Platzierung
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Elemente rückwärts einfügen für Stabilität
    for number in reversed(array):
        digit = (number // exp) % 10
        count[digit] -= 1
        output[count[digit]] = number

    return output


max_val = max(unsorted_array)
exp = 1

arr = unsorted_array.copy()

while max_val // exp > 0:
    arr = radix_sort(arr, exp)
    print(f"Nach Durchgang (exp={exp}):", arr)
    exp *= 10  # Zur nächsten Ziffernposition wechseln

print("\nsorted:", arr)

"""
original:           [170, 45, 75, 90, 802, 24, 2, 66]
after pass (exp=1): [170, 90, 802, 2, 24, 45, 75, 66]   ← sortiert nach Einerstelle
after pass (exp=10):[802, 2, 24, 45, 66, 170, 75, 90]   ← sortiert nach Zehnerstelle
after pass (exp=100):[2, 24, 45, 66, 75, 90, 170, 802]  ← sortiert nach Hunderterstelle

sorted: [2, 24, 45, 66, 75, 90, 170, 802]
"""
