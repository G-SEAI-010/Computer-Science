def find_words(words):
    """
    Zeitkomplexität: O(n × m)
      - n = Anzahl der Wörter
      - m = durchschnittliche Wortlänge
      - Für jedes Wort: Wir prüfen jedes Zeichen gegen die Reihen.
      - Set-Lookup (Suche in Mengen) ist O(1), also ist die Prüfung von m Zeichen O(m).
      - Gesamt: n Wörter × m Zeichen = O(n × m)

    Speicherkomplexität: O(1)
      - Drei Sets mit fester Größe (insgesamt 26 Buchstaben).
      - Die result-Liste zählt nicht zur Speicherkomplexität (da es die Ausgabe ist).
      - word_lower benötigt O(m) Platz, wird aber pro Schleifendurchlauf wiederverwendet und akkumuliert nicht.
      - Kein Speicherbedarf, der proportional zur Größe der Eingabe (n) wächst.
    """
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")

    rows = [row1, row2, row3]

    result = []

    for word in words:
        word_lower = word.lower()

        for row in rows:
            if all(char in row for char in word_lower):
                result.append(word)
                break

    return result


print("Lösung 1:")
print(find_words(["Hello", "Alaska", "Dad", "Peace"]))
print(find_words(["omk"]))
print(find_words(["adsdf", "sfd"]))

print()


# ------------------- Alternative Lösung -------------------


def find_words_set(words):
    """
    Zeitkomplexität: O(n × m)
      - n = Anzahl der Wörter
      - m = durchschnittliche Wortlänge
      - Das Erstellen von word_set benötigt O(m).
      - issubset() prüft jedes eindeutige Zeichen: O(k) wobei k (eindeutige Zeichen) ≤ m.
      - Gesamt: O(n × m)

    Speicherkomplexität: O(m)
      - word_set speichert die eindeutigen Zeichen des aktuellen Wortes.
      - Maximal m Zeichen (oder 26, falls das Wort extrem lang ist).
      - Temporärer Speicher, der nicht über die Schleifendurchläufe anwächst.
    """
    rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]

    result = []

    for word in words:
        word_set = set(word.lower())

        if any(word_set.issubset(row) for row in rows):
            result.append(word)

    return result


print("Lösung 2:")
print(find_words(["Hello", "Alaska", "Dad", "Peace"]))
print(find_words(["omk"]))
print(find_words(["adsdf", "sfd"]))

print()
