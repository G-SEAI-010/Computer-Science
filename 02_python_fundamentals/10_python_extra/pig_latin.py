import sys  # Ermöglicht den Zugriff auf Kommandozeilenparameter (sys.argv) und Programmabbruch (sys.exit)


def translate_word(word):
    """Übersetzt ein einzelnes Wort strikt nach den 3 Basis-Regeln."""

    # Wir definieren unsere Vokale als Referenz.
    # (Ohne 'y', um es für den Anfang einfach zu halten)
    vowels = "aeiou"

    # 1. ZUSTAND MERKEN & NORMALISIEREN
    # Wir prüfen, ob das Originalwort großgeschrieben ist (z.B. "Pig" -> True, "latin" -> False)
    is_capitalized = word.istitle()

    # Wir wandeln alles in Kleinbuchstaben um. Das spart uns später Arbeit,
    # weil wir nicht 'A' und 'a' separat prüfen müssen.
    word_lower = word.lower()

    # 2. DIE REGELN ANWENDEN (Kontrollfluss)
    # Regel 1: Beginnt mit einem Vokal
    # word_lower[0] greift auf den ersten Buchstaben des Wortes zu.
    if word_lower[0] in vowels:
        new_word = word_lower + "way"

    # Regel 3: Beginnt mit ZWEI Konsonanten
    # WICHTIG: Das muss VOR der Ein-Konsonant-Regel stehen, da sonst jedes Wort
    # mit zwei Konsonanten bereits in der Ein-Konsonant-Regel gefangen wird!
    elif (
        len(word_lower) > 1  # Schutz: Das Wort muss mindestens 2 Zeichen haben
        and word_lower[0] not in vowels  # 1. Buchstabe ist kein Vokal (also Konsonant)
        and word_lower[1] not in vowels  # 2. Buchstabe ist kein Vokal (also Konsonant)
    ):
        # Slicing: [2:] nimmt alles ab dem 3. Buchstaben, [:2] nimmt die ersten beiden.
        new_word = word_lower[2:] + word_lower[:2] + "ay"

    # Regel 2: Beginnt mit EINEM Konsonanten
    # Wenn es kein Vokal ist (if) und keine zwei Konsonanten (elif),
    # dann bleibt nur noch ein einzelner Konsonant am Anfang übrig.
    else:
        # Slicing: [1:] nimmt den Rest des Wortes, [0] nimmt den ersten Buchstaben.
        new_word = word_lower[1:] + word_lower[0] + "ay"

    # 3. ZUSTAND WIEDERHERSTELLEN
    # Wenn das Originalwort am Anfang groß war, machen wir unser neues Wort auch groß.
    if is_capitalized:
        return new_word.capitalize()
    else:
        return new_word


def main():
    # 1. EINGABE PRÜFEN
    # sys.argv enthält das Skript selbst (Index 0) und alle übergebenen Wörter.
    # Wenn die Länge kleiner als 2 ist, hat der Nutzer keine Wörter übergeben.
    if len(sys.argv) < 2:
        print("Bitte übergib einen Satz.")
        sys.exit(1)  # Beendet das Programm mit Fehlercode 1 (0 bedeutet fehlerfrei)

    # 2. DATEN VORBEREITEN
    # Wir schneiden den Namen der Python-Datei ab (Index 0) und speichern nur die echten Wörter.
    words = sys.argv[1:]

    # Eine leere Liste, in der wir gleich die fertigen Übersetzungen sammeln.
    translated_words = []

    # 3. VERARBEITEN
    # Wir gehen jedes Wort der Eingabe einzeln durch...
    for word in words:
        # ...schicken es an unsere Übersetzungs-Maschine und hängen das Ergebnis an die Liste an.
        translated_words.append(translate_word(word))

    # 4. AUSGABE
    # .join() nimmt unsere Liste und klebt sie zu einem Text zusammen, getrennt durch Leerzeichen.
    print(" ".join(translated_words))


# Startpunkt des Programms
main()
