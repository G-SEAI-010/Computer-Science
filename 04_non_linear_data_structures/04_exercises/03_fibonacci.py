# ==========================================
# Ansatz 1: Naive Rekursion (Sehr langsam!)
# ==========================================
# Zeitkomplexität: O(2^n)
# Jeder Funktionsaufruf verzweigt sich in zwei weitere Aufrufe. Dadurch verdoppelt
# sich die Anzahl der Operationen mit jedem Schritt, was zu exponentiellem #  Wachstum führt.
#
# Speicherkomplexität: O(n)
# Die maximale Tiefe des Rekursionsbaums (und damit des Call-Stacks im Arbeitsspeicher)
# entspricht n.


def fib_naive(n):
    if n <= 1:
        return n

    return fib_naive(n - 1) + fib_naive(n - 2)


#                     fib(5)
#                    /      \
#               fib(4)        fib(3)
#              /     \        /    \
#         fib(3)   fib(2)  fib(2)  fib(1)
#         /   \     /  \    /  \
#     fib(2) fib(1) ...  ... ...  ...
#      / \
# fib(1) fib(0)

# print(fib_naive(2))
# print(fib_naive(3))
# print(fib_naive(4))

# ==========================================
# Ansatz 2: Memoisation (Zwischenspeicherung)
# ==========================================

# Zeitkomplexität: O(n)
# Jede Fibonacci-Zahl von 0 bis n wird exakt einmal berechnet und das Ergebnis
# gespeichert (gecached). Folgeaufrufe laden das Ergebnis in O(1) aus dem Dictionary.
#
# Speicherkomplexität: O(n)
# Wir benötigen O(n) Speicher für das 'memo'-Dictionary und maximal O(n) Speicher
# für die Tiefe des rekursiven Call-Stacks.


def fib_memo(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# print(fib_memo(2))
# print(fib_memo(3))
# print(fib_memo(4))


# Schritt 1: fib(5) → nicht im memo
#   Aufruf fib(4) → nicht im memo
#     Aufruf fib(3) → nicht im memo
#       Aufruf fib(2) → nicht im memo
#         Aufruf fib(1) → gibt 1 zurück
#         Aufruf fib(0) → gibt 0 zurück
#       memo[2] = 1
#     Aufruf fib(2) → IM MEMO! gibt 1 zurück (keine Rekursion mehr!)
#     memo[3] = 2
#   Aufruf fib(3) → IM MEMO! gibt 2 zurück (keine Rekursion!)
#   memo[4] = 3
# Aufruf fib(3) → IM MEMO! gibt 2 zurück (keine Rekursion!)
# memo[5] = 5

from functools import cache


@cache  # Dekorator
def fib_pythonic(n):
    if n <= 1:
        return n
    return fib_pythonic(n - 1) + fib_pythonic(n - 2)


# print(fib_pythonic(2))
# print(fib_pythonic(3))
# print(fib_pythonic(4))

# ==========================================
# Ansatz 3: Iterativ (Optimal)
# ==========================================


def fib_iterative(n):
    """
    Zeitkomplexität: O(n)
      - Die Schleife läuft n-1 Mal (von 2 bis n).
      - Jeder Durchlauf führt nur einfache Additionen aus (konstanter Aufwand): O(1).
      - Gesamt: O(n)

    Speicherkomplexität: O(1) - AM BESTEN!
      - Es werden nur zwei Variablen gespeichert (prev, curr).
      - Es gibt keinen Rekursions-Stack (da keine Rekursion genutzt wird).
      - Es gibt kein Dictionary für Memoisation.
      - Der Speicherbedarf ist konstant, egal wie groß n wird.
    """

    if n <= 1:
        return n

    prev, curr = 0, 1

    for i in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr


# Start: prev = 0, curr = 1

# i = 2:  prev, curr = 1, 0+1 = 1, 1
# i = 3:  prev, curr = 1, 1+1 = 1, 2
# i = 4:  prev, curr = 2, 1+2 = 2, 3
# i = 5:  prev, curr = 3, 2+3 = 3, 5
# i = 6:  prev, curr = 5, 3+5 = 5, 8

# Gibt curr = 8 zurück.


# print(fib_iterative(2))
# print(fib_iterative(3))
# print(fib_iterative(40))
