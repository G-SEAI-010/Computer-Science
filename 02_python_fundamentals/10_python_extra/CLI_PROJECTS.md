# CLI-Projekte

## Übersicht

In diesen Projekten wendest du alles bisher Gelernte an, um drei kleine, aber vollständige Kommandozeilenprogramme (Command-Line Interface, CLI) zu programmieren. Jedes Projekt wird über das Terminal ausgeführt und empfängt Eingaben über `sys.argv`.

## `sys.argv` — Eingaben über das Terminal entgegennehmen

`sys.argv` funktioniert ermöglicht es dir, Daten direkt bei der Ausführung des Skripts über das Terminal zu übergeben.

```python
import sys

# sys.argv ist eine Liste von Strings (Zeichenketten)
# sys.argv[0] ist immer der Name des Skripts
# sys.argv[1] ist das erste übergebene Argument
# sys.argv[2] ist das zweite, und so weiter

print(sys.argv)
```

Führe das Skript so aus:

```bash
python script.py hallo welt
# ['script.py', 'hallo', 'welt']
```

Ein paar Dinge, die du beachten solltest:

* Alles in `sys.argv` ist ein **String**. Wandle es in `int` oder `float` um, wenn du Zahlen benötigst.
* Überprüfe immer die Länge mit `len(sys.argv)`, bevor du auf einen Index zugreifst, um Programmabstürze zu vermeiden.
* Wenn dein Argument Leerzeichen enthält, setze es in Anführungszeichen: `python script.py "hallo welt"`
* Um alle Argumente nach dem Skriptnamen als einen String zusammenzufassen: `" ".join(sys.argv[1:])`

```python
import sys

if len(sys.argv) < 2:
    print("Bitte übergib ein Argument")
else:
    name = sys.argv[1]
    print(f"Hallo, {name}!")
```

```bash
python script.py Alice
# Hallo, Alice!
```

## Projekt 1: Schere, Stein, Papier (Rock Paper Scissors)

Programmiere ein Schere-Stein-Papier-Spiel für die Kommandozeile.

### Anforderungen

* Nimm den Spielzug des Spielers als Eingabe über `sys.argv` entgegen.
* Generiere zufällig einen Spielzug für den Computer.
* Ermittle den Gewinner anhand der klassischen Regeln von Schere, Stein, Papier.
* Gib das Ergebnis (Gewonnen, Verloren oder Unentschieden) auf der Konsole aus.

### Ausführung

```bash
python rock_paper_scissors.py stein
```

### Erwartete Ausgabe

```text
Du hast Stein gewählt. Der Computer wählte Schere. Du gewinnst!
```

### Regelerinnerung

| **Spieler** | **Computer** | **Ergebnis**  |
| ----------- | ------------ | ------------- |
| Stein       | Schere       | Gewinn        |
| Schere      | Papier       | Gewinn        |
| Papier      | Stein        | Gewinn        |
| Beliebig    | Gleich       | Unentschieden |

> Tipp: Nutze das Modul `random`, um den Spielzug des Computers zu generieren.

## Projekt 2: Pig-Latin-Übersetzer

Erstelle ein Programm, das einen englischen Satz in die Spielsprache "Pig Latin" übersetzt.

### Anforderungen

* Nimm einen englischen Satz als Eingabe über `sys.argv` entgegen.
* Wandle jedes Wort gemäß den untenstehenden Pig-Latin-Regeln um.
* Gib den übersetzten Satz auf der Konsole aus.

### Pig-Latin-Regeln

| **Regel**                            | **Bedingung**                                      | **Beispiel**             |
| ------------------------------------ | -------------------------------------------------- | ------------------------ |
| Beginnt mit einem Vokal (Selbstlaut) | Hänge `way` ans Ende                               | `Awesome` → `Awesomeway` |
| Beginnt mit einem Konsonanten        | Verschiebe den Konsonanten ans Ende, hänge `ay` an | `Happy` → `Appyhay`      |
| Beginnt mit zwei Konsonanten         | Verschiebe beide ans Ende, hänge `ay` an           | `Child` → `Ildchay`      |

### Ausführung

```bash
python pig_latin.py Pig Latin is hard to speak
```

### Erwartete Ausgabe

```text
Igpay Atinlay isway ardhay otay eakspay
```

## Projekt 3: Caesar-Chiffre

Implementiere eine einfache Caesar-Chiffre — eine der ältesten Verschlüsselungstechniken der Welt.

### Anforderungen

* Nimm einen Satz und eine Verschiebungszahl (Shift) als Eingaben über `sys.argv` entgegen.
* Verschlüssele den Satz, indem du jeden Buchstaben um die angegebene Zahl verschiebst.
* Nicht-Buchstaben-Zeichen (Leerzeichen, Satzzeichen) bleiben unverändert.
* Groß-/Kleinschreibung wird ignoriert — die Ausgabe ist komplett in Kleinbuchstaben.
* Eine negative Verschiebung bewegt Buchstaben nach links, eine positive Verschiebung nach rechts.

### Ausführung

```bash
python caesar_cipher.py "hello world" 3
```

### Erwartete Ausgabe

```text
khoor zruog
```

### Wie die Verschiebung funktioniert

```text
a b c d e f g h i j k l m n o p q r s t u v w x y z
            Verschiebung um 3 nach rechts →
d e f g h i j k l m n o p q r s t u v w x y z a b c

h → k
e → h
l → o
o → r
```

> Tipp: Die Python-Funktionen `ord()` und `chr()` wandeln zwischen Zeichen und ihren ASCII-Zahlen um. `% 26` hilft dir dabei, am Ende des Alphabets wieder von vorne zu beginnen (Wrap-around).

## Erste Schritte

1. Erstelle für jedes Projekt eine neue `.py`-Datei.
2. Beginne mit dem Setup für `sys.argv` und nutze einen `print`-Befehl, um zu überprüfen, ob deine Eingaben korrekt im Skript ankommen.
3. Programmiere und teste immer nur eine Funktion auf einmal, bevor du am Ende alles zusammenfügst.

---

## Exkurs: Interaktive Eingaben mit `input()`

In den obigen Projekten fokussieren wir uns auf `sys.argv`, um Daten direkt beim Startbefehl zu übergeben. Das nennt man **Kommandozeilenparameter**.

Theoretisch könntest du Eingaben aber auch interaktiv abfragen, **während** das Programm bereits läuft. Dafür nutzt Python die integrierte Funktion `input()`.

So funktioniert es:

```python
# Das Programm pausiert hier und wartet auf die Benutzereingabe
name = input("Bitte gib deinen Namen ein: ")
print(f"Hallo, {name}!")
```

Wenn du dieses Skript ausführst (`python script.py`), passiert Folgendes:

1. Das Programm startet.
2. Es gibt den Text `"Bitte gib deinen Namen ein: "` auf der Konsole aus.
3. Es **pausiert**, bis der Nutzer etwas eintippt und die *Enter*-Taste drückt.
4. Die Eingabe wird (immer als String!) in der Variablen `name` gespeichert und das Programm läuft weiter.

**Wann nutzt man was?**

* **`sys.argv`**: Perfekt für Skripte, die automatisiert oder von anderen Programmen aufgerufen werden sollen. Man übergibt die Daten in einem Rutsch und das Programm rattert durch.
* **`input()`**: Perfekt für interaktive Programme, Text-Adventures oder Menüs, bei denen der Benutzer Schritt für Schritt durch einen Prozess geführt wird.
