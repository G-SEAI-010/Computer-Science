print("--- Dijkstra's Algorithm (Undirected) ---\n")


class UndirectedGraph:
    def __init__(self, labels):
        """Initialisiert einen ungerichteten Graphen."""
        self.labels = labels
        self.num_vertices = len(labels)
        self.adj_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]

    def label_to_index(self, label):
        """Konvertiert Label zu Index."""
        if label not in self.labels:
            raise ValueError(f"Label {label} nicht gefunden.")
        return self.labels.index(label)

    def add_edge(self, label1, label2, weight=1):
        """Fügt eine ungerichtete Kante hinzu."""
        u = self.label_to_index(label1)
        v = self.label_to_index(label2)
        self.adj_matrix[u][v] = weight
        self.adj_matrix[v][u] = weight

    def print_matrix(self):
        """Gibt die Adjazenzmatrix aus."""
        header = "   " + "  ".join(self.labels)
        print(header)
        for i, row in enumerate(self.adj_matrix):
            row_str = "  ".join(str(x) for x in row)
            print(f"{self.labels[i]}  {row_str}")


def dijkstra(graph, start_label):
    """
    Dijkstra-Algorithmus zur Berechnung kürzester Pfade.

    Args:
        graph: UndirectedGraph Instanz
        start_label: Startknoten-Label

    Returns:
        Dictionary {label: kürzeste_distanz}
    """
    labels = graph.labels
    n = graph.num_vertices

    # INITIALISIERUNGSPHASE
    # dist[i] = kürzeste bekannte Distanz vom Start zu Knoten i
    dist = [float("inf")] * n

    # visited[i] = wurde optimaler Pfad bereits gefunden?
    visited = [False] * n

    # Startknoten hat Distanz 0
    start_index = labels.index(start_label)
    dist[start_index] = 0

    # HAUPTSCHLEIFE
    # Jeden Knoten genau einmal verarbeiten
    for _ in range(n):
        # SCHRITT 1: Finde unbesuchten Knoten mit kleinster Distanz
        min_dist = float("inf")
        min_vertex = -1

        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_vertex = i

        # Kein erreichbarer Knoten mehr
        if min_vertex == -1:
            break

        # SCHRITT 2: Markiere als besucht (optimal gefunden)
        visited[min_vertex] = True

        # SCHRITT 3: Relaxiere alle Kanten vom aktuellen Knoten
        for neighbor in range(n):
            weight = graph.adj_matrix[min_vertex][neighbor]

            # Nur existierende Kanten zu unbesuchten Nachbarn
            if weight > 0 and not visited[neighbor]:
                new_dist = dist[min_vertex] + weight

                # Relaxation: Verbesserte Distanz gefunden?
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist

    # Ergebnis formatieren
    result = {}
    for i, label in enumerate(labels):
        result[label] = dist[i] if dist[i] != float("inf") else None
    return result


# Beispiel
labels = ["A", "B", "C", "D", "E", "F"]
graph = UndirectedGraph(labels)

# Kanten hinzufügen
#     A --4-- B
#     |       |
#     5      11
#     |       |
#     C --3-- E --6-- F
#             |       |
#            13       |
#             D --2-- +

edges = [
    ("A", "B", 4),
    ("A", "C", 5),
    ("B", "C", 11),
    ("B", "D", 9),
    ("B", "E", 7),
    ("C", "E", 3),
    ("D", "E", 13),
    ("D", "F", 2),
    ("E", "F", 6),
]

for label1, label2, weight in edges:
    graph.add_edge(label1, label2, weight)

print("Adjazenzmatrix:")
graph.print_matrix()

print()

result = dijkstra(graph, "A")

print(result)


print("--- Dijkstra's Algorithm (Directed) ---\n")


class DirectedGraph:
    def __init__(self, labels):
        """Initialisiert einen gerichteten Graphen."""
        self.labels = labels
        self.num_vertices = len(labels)
        self.adj_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]

    def label_to_index(self, label):
        if label not in self.labels:
            raise ValueError(f"Label {label} nicht gefunden.")
        return self.labels.index(label)

    def add_edge(self, label_from, label_to, weight=1):
        """Fügt eine gerichtete Kante hinzu."""
        u = self.label_to_index(label_from)
        v = self.label_to_index(label_to)
        self.adj_matrix[u][v] = weight

    def print_matrix(self):
        """Gibt die Adjazenzmatrix aus."""
        header = "    " + "  ".join(self.labels)
        print(header)
        for i, row in enumerate(self.adj_matrix):
            row_str = "  ".join(str(x) for x in row)
            print(f"{self.labels[i]}   {row_str}")


def dijkstra(graph, start_label):
    """
    Dijkstra-Algorithmus (funktioniert für gerichtet und ungerichtet identisch!)
    """
    labels = graph.labels
    n = graph.num_vertices

    dist = [float("inf")] * n
    visited = [False] * n

    start_index = labels.index(start_label)
    dist[start_index] = 0

    for _ in range(n):
        min_dist = float("inf")
        min_vertex = -1

        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_vertex = i

        if min_vertex == -1:
            break

        visited[min_vertex] = True

        # Bei gerichteten Graphen: folge nur ausgehenden Kanten
        for neighbor in range(n):
            weight = graph.adj_matrix[min_vertex][neighbor]

            if weight > 0 and not visited[neighbor]:
                new_dist = dist[min_vertex] + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist

    result = {}
    for i, label in enumerate(labels):
        result[label] = dist[i] if dist[i] != float("inf") else None
    return result


# Beispiel
labels = ["A", "B", "C", "D", "E", "F"]
graph = DirectedGraph(labels)

# Gerichtete Kanten
edges = [
    ("A", "B", 4),
    ("A", "C", 5),
    ("B", "C", 11),
    ("B", "D", 9),
    ("B", "E", 7),
    ("C", "E", 3),
    ("D", "E", 13),
    ("D", "F", 2),
    ("E", "F", 6),
]

for label_from, label_to, weight in edges:
    graph.add_edge(label_from, label_to, weight)

print("Adjazenzmatrix (gerichtet):")
graph.print_matrix()

print()

result = dijkstra(graph, "A")

print(result)

print("--- Dijkstra's Algorithm (Pfad-Rekonstruktion) ---\n")


def dijkstra_with_path(graph, start_label):
    """
    Dijkstra mit Pfad-Rekonstruktion.
    Gibt nicht nur Distanz, sondern auch den tatsächlichen Pfad.
    """
    labels = graph.labels
    n = graph.num_vertices

    dist = [float("inf")] * n
    visited = [False] * n
    # prev[i] = welcher Knoten war der vorherige Knoten im optimalen Pfad zu i?
    prev = [-1] * n

    start_index = labels.index(start_label)
    dist[start_index] = 0

    for _ in range(n):
        min_dist = float("inf")
        min_vertex = -1

        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_vertex = i

        if min_vertex == -1:
            break

        visited[min_vertex] = True

        for neighbor in range(n):
            weight = graph.adj_matrix[min_vertex][neighbor]

            if weight > 0 and not visited[neighbor]:
                new_dist = dist[min_vertex] + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    prev[neighbor] = min_vertex  # ← Speichere vorherigen Knoten

    # Pfad rekonstruieren
    def reconstruct_path(end_index):
        """Rekonstruiert Pfad vom Start zum Ende."""
        path = []
        current = end_index
        while current != -1:
            path.append(labels[current])
            current = prev[current]
        path.reverse()
        return path if path[0] == start_label else None

    result = {}
    for i, label in enumerate(labels):
        path = reconstruct_path(i)
        distance = dist[i] if dist[i] != float("inf") else None
        result[label] = {"distance": distance, "path": path}
    return result


# Verwendung
result = dijkstra_with_path(graph, "A")
print("\nKürzeste Pfade mit Routen von A:")
for label, info in sorted(result.items()):
    if info["distance"] is not None:
        print(
            f"  A → {label}: Distanz={info['distance']}, Pfad={' → '.join(info['path'])}"
        )

print("--- Dijkstra's Algorithm (Min-Heap) ---\n")

import heapq


def dijkstra_heap(graph, start_label):
    """Dijkstra mit Min-Heap."""
    labels = graph.labels
    n = graph.num_vertices

    dist = [float("inf")] * n
    start_index = labels.index(start_label)
    dist[start_index] = 0

    # Heap enthält Tupel (distanz, knoten_index)
    heap = [(0, start_index)]

    while heap:
        current_dist, u = heapq.heappop(heap)

        # Überspringe, wenn wir bereits einen besseren Pfad gefunden haben
        if current_dist > dist[u]:
            continue

        # Relaxiere alle Kanten
        for v in range(n):
            weight = graph.adj_matrix[u][v]
            if weight > 0:
                new_dist = dist[u] + weight
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))

    return dist
