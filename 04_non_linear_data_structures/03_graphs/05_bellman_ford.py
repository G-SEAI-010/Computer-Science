print("\n--- Bellman-Ford mit Adjazenzmatrix ---\n")


class DirectedGraph:
    def __init__(self, labels):
        self.labels = labels
        self.num_vertices = len(labels)
        self.adj_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]

    def label_to_index(self, label):
        if label not in self.labels:
            raise ValueError(f"Label {label} nicht im Graphen gefunden.")
        return self.labels.index(label)

    def add_edge(self, label_from, label_to, weight=1):
        u = self.label_to_index(label_from)
        v = self.label_to_index(label_to)
        self.adj_matrix[u][v] = weight

    def remove_edge(self, label_from, label_to):
        u = self.label_to_index(label_from)
        v = self.label_to_index(label_to)
        self.adj_matrix[u][v] = 0

    def print_matrix(self):
        header = "    " + "  ".join(self.labels)
        print(header)
        for i, row in enumerate(self.adj_matrix):
            row_str = "  ".join(str(x) for x in row)
            print(f"{self.labels[i]}   {row_str}")


# Einen gerichteten Graphen mit diesen Labels erstellen
labels = ["A", "B", "C", "D", "E"]
graph = DirectedGraph(labels)
matrix = [
    [0, 0, 4, 0, 5],
    [0, 0, -4, 0, 0],
    [-3, 0, 0, 0, 0],
    [4, 0, 7, 0, 3],
    [0, 2, 3, 0, 0],
]
# Die Adjazenzmatrix des Graphen zu Demonstrationszwecken direkt befüllen
graph.adj_matrix = matrix
print("Adjazenzmatrix des gerichteten Graphen:")
graph.print_matrix()


# Implementierung des Bellman-Ford-Algorithmus
def bellman_ford(graph, start_label):
    """
    Berechnet die kürzesten Pfade von 'start_label' zu allen anderen Knoten,
    wobei negative Kantengewichte zulässig sind.
    Wenn ein negativer Zyklus erkannt wird (der vom Start aus erreichbar ist),
    wird dies im Ergebnis vermerkt.

    Gibt ein Dict in folgendem Format zurück:
    {
      'distances': { label: kosten (oder None wenn unerreichbar) },
      'negative_cycle': bool (True wenn ein negativer Zyklus erkannt wurde)
    }
    """
    labels = graph.labels
    n = graph.num_vertices

    # INITIALISIERUNGSPHASE
    # --------------------
    # dist[i]: beste bekannte Distanz vom Start zu Knoten i
    # Alle Distanzen auf Unendlich setzen (bedeutet "noch kein Pfad gefunden")
    dist = [float("inf")] * n

    # Distanz des Startknotens auf 0 setzen (Distanz von A nach A ist 0)
    start_index = labels.index(start_label)
    dist[start_index] = 0

    # HAUPTALGORITHMUS: Alle Kanten V-1 Mal relaxieren
    # ------------------------------------------
    # Warum V-1? Der längste einfache Pfad (ohne wiederholte Knoten) hat höchstens V-1 Kanten.
    # Jede Iteration erlaubt es Pfaden, sich um eine weitere Kante auszudehnen.
    # Nach V-1 Iterationen sind garantiert alle kürzesten Pfade gefunden.
    for iteration in range(n - 1):
        # ALLE Kanten im Graphen verarbeiten (die Reihenfolge ist egal)
        # Im Gegensatz zu Dijkstra wählen wir Knoten nicht "greedy" aus - wir prüfen alles

        for u in range(n):  # Für jeden Quellknoten u
            for v in range(n):  # Für jeden potenziellen Zielknoten v
                weight = graph.adj_matrix[u][v]

                # Prüfen, ob die Kante u → v existiert (Gewicht != 0)
                # UND ob wir bereits einen Pfad zu u gefunden haben (dist[u] != Unendlich)
                if weight != 0 and dist[u] != float("inf"):
                    # Potenzielle neue Distanz zu v über u berechnen
                    new_dist = dist[u] + weight

                    # KANTENRELAXATION: Wenn dieser Pfad kürzer ist, aktualisieren
                    # Dies ist das Herzstück des Algorithmus
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        # Hinweis: Wir können JEDEN Knoten aktualisieren, auch wenn er schon zuvor aktualisiert wurde.
                        # Genau deshalb kann Bellman-Ford mit negativen Gewichten umgehen!

    # PHASE ZUR ERKENNUNG NEGATIVER ZYKLEN
    # -------------------------------
    # Nach V-1 Iterationen sollten alle kürzesten Pfade gefunden sein.
    # Wenn wir eine Distanz IMMER NOCH verbessern können, gibt es einen negativen Zyklus.
    negative_cycle = False

    for u in range(n):
        for v in range(n):
            weight = graph.adj_matrix[u][v]

            # Prüfen, ob die Kante existiert und die Quelle erreichbar ist
            if weight != 0 and dist[u] != float("inf"):
                # Wenn wir diese Kante immer noch relaxieren können, existiert ein negativer Zyklus!
                if dist[u] + weight < dist[v]:
                    # Das bedeutet, wir können immer weiter im Kreis laufen
                    # und die Distanz nimmt stetig ab (nähert sich -∞)
                    negative_cycle = True
                    break
        if negative_cycle:
            break

    # ERGEBNIS-FORMATIERUNG
    # -----------------
    # Das Distanz-Array in ein lesbareres Dictionary-Format umwandeln
    # Nutze None für unerreichbare Knoten (die immer noch auf unendlich stehen)
    distance_dict = {}
    for i, label in enumerate(labels):
        distance_dict[label] = dist[i] if dist[i] != float("inf") else None

    return {"distances": distance_dict, "negative_cycle": negative_cycle}


result = bellman_ford(graph, "A")

print()

print("Kürzeste Pfadkosten von A:\n")
for vertex, cost in result["distances"].items():
    print(f"{vertex}: Kosten = {cost}")

print()

# Optional kannst du ausgeben, ob ein negativer Zyklus erreichbar ist:
if result["negative_cycle"]:
    print("Ein negativer Zyklus ist von A aus erreichbar.")
else:
    print("Kein negativer Zyklus ist von A aus erreichbar.")


print("\n--- Bellman-Ford mit Adjazenzliste ---\n")


class DirectedGraph:
    def __init__(self, labels):
        self.labels = labels
        self.num_vertices = len(labels)
        # Statt einer Matrix (NxN Nullen) erstellen wir eine Liste von leeren Listen
        self.adj_list = [[] for _ in range(self.num_vertices)]

    def label_to_index(self, label):
        if label not in self.labels:
            raise ValueError(f"Label {label} nicht im Graphen gefunden.")
        return self.labels.index(label)

    def add_edge(self, label_from, label_to, weight=1):
        u = self.label_to_index(label_from)
        v = self.label_to_index(label_to)
        # Wir hängen Zielknoten und Gewicht als Tuple an die Liste des Startknotens an
        self.adj_list[u].append((v, weight))

    def remove_edge(self, label_from, label_to):
        u = self.label_to_index(label_from)
        v = self.label_to_index(label_to)
        # Wir behalten alle Kanten in der Liste, außer der, die zum Zielknoten v führt
        self.adj_list[u] = [(node, w) for node, w in self.adj_list[u] if node != v]

    def print_graph(self):
        """Ersetzt print_matrix und gibt die Adjazenzliste lesbar aus."""
        for i, edges in enumerate(self.adj_list):
            edge_strs = [f"({self.labels[v]}, Gewicht: {w})" for v, w in edges]
            print(
                f"{self.labels[i]} -> {', '.join(edge_strs) if edge_strs else 'Keine ausgehenden Kanten'}"
            )


# Einen gerichteten Graphen mit diesen Labels erstellen
labels = ["A", "B", "C", "D", "E"]
graph = DirectedGraph(labels)

# Die alten Matrix-Daten (zur einfachen Übernahme)
matrix = [
    [0, 0, 4, 0, 5],
    [0, 0, -4, 0, 0],
    [-3, 0, 0, 0, 0],
    [4, 0, 7, 0, 3],
    [0, 2, 3, 0, 0],
]

# Wir überschreiben nicht mehr blind eine Eigenschaft, sondern nutzen
# sauberes Einfügen via add_edge, um die Adjazenzliste aus der Matrix aufzubauen.
for u in range(len(labels)):
    for v in range(len(labels)):
        weight = matrix[u][v]
        if weight != 0:
            graph.add_edge(labels[u], labels[v], weight)

print("Adjazenzliste des gerichteten Graphen:")
graph.print_graph()


# Implementierung des Bellman-Ford-Algorithmus
def bellman_ford(graph, start_label):
    """
    Berechnet die kürzesten Pfade von 'start_label' zu allen anderen Knoten.
    Nutzt eine Adjazenzliste für verbesserte Performance (O(V * E)).
    """
    labels = graph.labels
    n = graph.num_vertices

    # INITIALISIERUNGSPHASE
    dist = [float("inf")] * n
    start_index = labels.index(start_label)
    dist[start_index] = 0

    # HAUPTALGORITHMUS
    for iteration in range(n - 1):
        updated_in_this_round = False

        for u in range(n):
            # OPTIMIERUNG: Wenn Knoten u vom Start noch gar nicht erreichbar ist,
            # müssen wir seine ausgehenden Kanten nicht prüfen.
            if dist[u] == float("inf"):
                continue

            # ÄNDERUNG: Statt "for v in range(n)" prüfen wir NUR die echten Nachbarn!
            for v, weight in graph.adj_list[u]:
                new_dist = dist[u] + weight

                # KANTENRELAXATION
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    updated_in_this_round = True

        # EARLY EXIT OPTIMIERUNG: Wenn im gesamten Graph nichts mehr billiger wurde,
        # sind wir bereits fertig und können uns die restlichen Iterationen sparen.
        if not updated_in_this_round:
            break

    # PHASE ZUR ERKENNUNG NEGATIVER ZYKLEN
    negative_cycle = False

    for u in range(n):
        if dist[u] == float("inf"):
            continue

        # Auch hier: Nur echte Nachbarn prüfen
        for v, weight in graph.adj_list[u]:
            if dist[u] + weight < dist[v]:
                negative_cycle = True
                break
        if negative_cycle:
            break

    # ERGEBNIS-FORMATIERUNG
    distance_dict = {}
    for i, label in enumerate(labels):
        distance_dict[label] = dist[i] if dist[i] != float("inf") else None

    return {"distances": distance_dict, "negative_cycle": negative_cycle}


result = bellman_ford(graph, "A")

print("\nKürzeste Pfadkosten von A:")
for vertex, cost in result["distances"].items():
    print(f"{vertex}: kosten = {cost}")

print()

# Optional ausgeben, ob ein negativer Zyklus erreichbar ist:
if result["negative_cycle"]:
    print("ACHTUNG: Ein negativer Zyklus ist von A aus erreichbar.")
else:
    print("Kein negativer Zyklus ist von A aus erreichbar.")
