# ==========================================
# Ansatz 1: BFS (Breitensuche / Breadth-First Search)
# ==========================================

from collections import deque, defaultdict

# Zeitkomplexität: O(V + E)
# - V steht für Vertices (Anzahl der Knoten 'n') und E für Edges (Anzahl der Kanten).
# - Wir verarbeiten jeden Knoten maximal einmal (wenn er aus der Warteschlange geholt wird).
# - Wir iterieren über jede Kante maximal zweimal (einmal von jedem der beiden verbundenen Knoten),
#   um die Nachbarn zu prüfen.
# - Das initiale Aufbauen der Adjazenzliste dauert ebenfalls O(E).
#
# Speicherkomplexität: O(V + E) (Zusätzlicher Speicher)
# - Die Adjazenzliste (graph) benötigt O(V + E) Speicherplatz, um alle Verbindungen abzubilden.
# - Die Warteschlange (queue) und das Boolean-Array (visited) benötigen im schlimmsten Fall
#   jeweils O(V) Platz (z. B. wenn die Queue alle Knoten einer sehr breiten Ebene hält).


def valid_path_bfs(n, edges, source, destination):
    # Schneller Abbruch: Wenn wir schon am Ziel stehen, existiert der Pfad offensichtlich.
    if source == destination:
        return True

    # GRAPHEN AUFBAUEN (Adjazenzliste)
    # defaultdict(list) ist extrem praktisch: Wenn wir auf einen Schlüssel zugreifen,
    # der noch nicht existiert (z.B. graph[0]), wird automatisch eine leere Liste [] erstellt.
    graph = defaultdict(list)
    for u, v in edges:
        # Da der Graph ungerichtet ist, müssen wir die Verbindung in beide Richtungen eintragen.
        graph[u].append(v)
        graph[v].append(u)

    # WARTESCHLANGE INITIALISIEREN (FIFO - First In, First Out)
    # deque (Double-Ended Queue) wird verwendet, weil popleft() O(1) Zeit benötigt.
    # Bei einer normalen Liste würde pop(0) alle restlichen Elemente verschieben und O(N) dauern!
    queue = deque([source])

    # BESUCHT-LISTE (Visited Array)
    # Ein Boolean-Array ist bei fortlaufenden Knoten-IDs (0 bis n-1) viel speichereffizienter
    # und schneller beim Nachschlagen (O(1)) als ein Python-Set.
    visited = [False] * n

    # Markiere den Startpunkt sofort als besucht, damit wir ihn nicht versehentlich
    # später nochmal in die Warteschlange packen.
    visited[source] = True

    # TRAVERSIERUNG
    # Solange wir noch unerkundete Knoten in der Warteschlange haben...
    while queue:
        # Nimm den ältesten Knoten von VORNE aus der Schlange (Ausbreitung wie eine Wasserwelle)
        node = queue.popleft()

        # Prüfe alle Nachbarn des aktuellen Knotens
        for neighbor in graph[node]:
            # OPTIMIERUNG: Haben wir das Ziel gefunden?
            # Wir prüfen das, BEVOR wir den Nachbarn in die Queue stecken. Das spart Zeit!
            if neighbor == destination:
                return True

            # Wenn der Nachbar noch unbesucht ist...
            if not visited[neighbor]:
                # 1. Sofort als besucht markieren
                visited[neighbor] = True
                # 2. Hinten in die Warteschlange einreihen, um später seine Nachbarn zu prüfen
                queue.append(neighbor)

    # Wenn die Warteschlange leer ist und das Ziel nie erreicht wurde
    return False


# ==========================================
# Schritt-für-Schritt (Ansatz 1)
# ==========================================
# Beispiel: n=3, edges=[[0,1],[1,2],[2,0]], source=0, dest=2

# Adjazenzliste nach dem Aufbau: {0: [1, 2], 1: [0, 2], 2: [1, 0]}

# Anfangszustand:
#   queue = deque([0])
#   visited = [True, False, False]  # Entspricht den Indizes 0, 1, 2

# Iteration 1:
#   Pop node = 0
#   Nachbarn von 0: [1, 2]
#     - Ist 1 == 2? Nein. Besucht? Nein → markiere als besucht, hänge in die Queue.
#     - Ist 2 == 2? JA! ✓

# Rückgabe: True

# Der Pfad wurde direkt beim ersten Überprüfen der direkten Nachbarn gefunden!


print(valid_path_bfs(3, [[0, 1], [1, 2], [2, 0]], 0, 2))
print(valid_path_bfs(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))

# ===========================================================
# Ansatz 2: DFS (Iterative Tiefensuche / Depth-First Search)
# ===========================================================


# Zeitkomplexität: O(V + E)
# - Genau wie bei der BFS: Wir verarbeiten jeden Knoten maximal einmal (beim Pop vom Stack)
#   und evaluieren jede Kante maximal zweimal.
#
# Speicherkomplexität: O(V + E) (Zusätzlicher Speicher)
# - Die Adjazenzliste benötigt O(V + E).
# - Der explizite Stack und das Visited-Array benötigen maximal O(V) Platz (z. B. bei einem
#   Graphen, der wie eine gerade Linie aussieht und alle Knoten auf den Stack gepusht werden).


def valid_path_dfs(n, edges, source, destination):
    if source == destination:
        return True

    # GRAPHEN AUFBAUEN (Exakt wie bei der BFS)
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # STACK INITIALISIEREN (LIFO - Last In, First Out)
    # Eine normale Python-Liste eignet sich perfekt als Stack.
    # Warum iterativ und nicht rekursiv? Um das Python-Rekursionslimit (RecursionError)
    # bei extrem tiefen Graphen zu vermeiden!
    stack = [source]

    visited = [False] * n
    visited[source] = True

    while stack:
        # Nimm den NEUESTEN Knoten von HINTEN vom Stack (Tiefensuche: Wir tauchen sofort tief ein)
        node = stack.pop()

        for neighbor in graph[node]:
            if neighbor == destination:
                return True

            if not visited[neighbor]:
                visited[neighbor] = True
                # Den Nachbarn OBEN auf den Stack legen, damit wir in der nächsten Iteration
                # direkt bei diesem Nachbarn (und nicht bei einem Geschwister-Knoten) weitermachen.
                stack.append(neighbor)

    return False


# Adjazenzliste: {0: [1], 1: [0, 2], 2: [1]}

# Anfangszustand:
#   stack = [0]
#   visited = [True, False, False]

# Iteration 1:
#   Pop node = 0
#   Nachbarn von 0: [1]
#     - Ist 1 == 2? Nein. Besucht? Nein → markieren, auf den Stack legen.

#   stack = [1]
#   visited = [True, True, False]

# Iteration 2:
#   Pop node = 1
#   Nachbarn von 1: [0, 2]
#     - Ist 0 == 2? Nein. Besucht? Ja → überspringen.
#     - Ist 2 == 2? JA! ✓

# Rückgabe: True

print(valid_path_dfs(3, [[0, 1], [1, 2], [2, 0]], 0, 2))
print(valid_path_dfs(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))

# ===========================================================
# Ansatz 3: UnionFind (???)
# ===========================================================


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


def valid_path(n, edges, source, destination):
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return uf.connected(source, destination)
