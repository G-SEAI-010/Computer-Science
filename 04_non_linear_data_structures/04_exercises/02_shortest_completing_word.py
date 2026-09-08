from collections import Counter


def shortest_completing_word(licensePlate, words):
    """
    Zeitkomplexität: O(L + n * m) im Worst Case, optimiert in der Praxis
      - L = Länge des Nummernschilds
      - n = Anzahl der Wörter
      - m = Durchschnittliche Länge eines Wortes
      - plate_count erstellen: O(L)
      - Längenprüfung (len): O(1) pro Wort
      - Counter & Subtraktion: O(m) pro geprüftem Wort
      - Worst Case O(L + n * m): Die Wörter sind absteigend nach Länge sortiert.
      - Best/Average Case O(L + n + m): Ein kurzes gültiges Wort wird früh gefunden.
        Die meisten Folgeprüfungen brechen dank O(1) Längen-Check ab.

    Speicherkomplexität: O(1) (bzw. O(k) mit k <= 26)
      - Maximal 26 Schlüssel-Wert-Paare im plate_count (Alphabet).
      - Maximal 26 Schlüssel-Wert-Paare im temporären Counter(word).
      - Da die Maximalgröße unabhängig von der Eingabe fest auf 26 begrenzt ist,
        ist der Speicherbedarf konstant O(1).
    """
    plate_count = Counter(char.lower() for char in licensePlate if char.isalpha())
    # plate_count = Counter({'s': 2, 'p': 1, 't': 1})

    shortest = None

    for word in words:
        if shortest is not None and len(word) >= len(shortest):
            continue
        if not (plate_count - Counter(word)):
            shortest = word

    return shortest
