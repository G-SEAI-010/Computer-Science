print("--- DFS Graph Traversal (Undirected) ---\n")


class UndirectedGraph:
    def __init__(self, labels):
        """Initialisiert einen ungerichteten Graphen."""
        self.labels = labels  # z. B. ["A", "B", "C", "D"]
        self.num_vertices = len(labels)
        self.adj_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def label_to_index(self, label):
        """Konvertiert ein Knoten-Label in seinen Matrix-Index."""
        if label not in self.labels:
            raise ValueError(f"Label {label} nicht im Graphen gefunden.")
        return self.labels.index(label)

    def add_edge(self, label1, label2, weight=1):
        """Fügt eine Kante zwischen zwei Knoten hinzu (beide Richtungen)."""
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

    def dfs(self, start_label):
        """
        Führt eine DFS-Traversierung ausgehend vom Knoten mit dem Label 'start_label' durch.

        DFS erkundet jeden Zweig so weit wie möglich, bevor es zum Backtracking kommt.
        Es nutzt Rekursion (welche implizit den Call-Stack verwendet).
        """
        visited = set()

        def dfs_helper(label):
            """Rekursive Hilfsfunktion für DFS."""
            # Schritt 1: Den aktuellen Knoten besuchen
            print(label)

            # Schritt 2: Als besucht markieren (Zyklen vermeiden)
            visited.add(label)

            # Schritt 3: Index des aktuellen Knotens abrufen
            current_index = self.label_to_index(label)

            # Schritt 4: Alle benachbarten Knoten erkunden
            for neighbor_index, is_connected in enumerate(
                self.adj_matrix[current_index]
            ):
                neighbor_label = self.labels[neighbor_index]

                # Schritt 5: Wenn unbesucht, rekursiv in Tiefe gehen
                if is_connected and neighbor_label not in visited:
                    dfs_helper(neighbor_label)

            # Schritt 6: Backtrack zum vorherigen Knoten

        # Starte DFS vom Startknoten
        dfs_helper(start_label)


# Beispiel
labels = ["A", "B", "C", "D"]
graph = UndirectedGraph(labels)

# Kanten hinzufügen
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("A", "D")
graph.add_edge("B", "C")

print("Adjazenzmatrix:")
graph.print_matrix()

print("\nDFS-Traversierung ab Knoten A:")
graph.dfs("A")
# Ausgabe: A → B → C → D (oder ähnliche Reihenfolge je nach Nachbarn-Speicherung)

# -----------------------------------------------------------------------------------------

print("\n--- BFS Graph Traversal (Undirected) ---\n")

from collections import deque


class UndirectedGraph:
    def __init__(self, labels):
        """Initialisiert einen ungerichteten Graphen."""
        self.labels = labels
        self.num_vertices = len(labels)
        self.adj_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def label_to_index(self, label):
        """Konvertiert ein Knoten-Label in seinen Matrix-Index."""
        if label not in self.labels:
            raise ValueError(f"Label {label} nicht im Graphen gefunden.")
        return self.labels.index(label)

    def add_edge(self, label1, label2, weight=1):
        """Fügt eine Kante zwischen zwei Knoten hinzu."""
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

    def bfs(self, start_label):
        """
        Führt eine BFS-Traversierung ausgehend vom Knoten mit dem Label 'start_label' durch.

        BFS erkundet den Graphen Ebene für Ebene und besucht alle Nachbarn
        auf der aktuellen Ebene, bevor zur nächsten Ebene übergegangen wird.
        Es nutzt eine Queue (FIFO).
        """
        visited = set()
        queue = deque()  # Besser als liste mit pop(0) — O(1) statt O(n)

        # Schritt 1: Mit dem Startknoten beginnen
        queue.append(start_label)
        visited.add(start_label)

        # Schritt 2: Knoten verarbeiten, bis die Queue leer ist
        while queue:
            # Schritt 3: Den vordersten Knoten entnehmen (FIFO)
            current_label = queue.popleft()

            # Schritt 4: Diesen Knoten verarbeiten
            print(current_label)

            # Schritt 5: Index des aktuellen Knotens abrufen
            current_index = self.label_to_index(current_label)

            # Schritt 6: Alle unbesuchten benachbarten Knoten in Queue einreihen
            for neighbor_index, is_connected in enumerate(
                self.adj_matrix[current_index]
            ):
                neighbor_label = self.labels[neighbor_index]

                # Schritt 7: Wenn unbesucht, zur Queue hinzufügen
                if is_connected and neighbor_label not in visited:
                    queue.append(neighbor_label)
                    # WICHTIG: JETZT als besucht markieren, nicht erst beim Entnehmen
                    # Dies verhindert, dass derselbe Knoten mehrfach zur Queue hinzugefügt wird
                    visited.add(neighbor_label)


# Beispiel
labels = ["A", "B", "C", "D"]
graph = UndirectedGraph(labels)

# Kanten hinzufügen
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("A", "D")
graph.add_edge("B", "C")

print("Adjazenzmatrix:")
graph.print_matrix()

print("\nBFS-Traversierung ab Knoten A:")
graph.bfs("A")
# Ausgabe: A → B → C → D (Ebene 0, dann Ebene 1)

# -----------------------------------------------------------------------------------------

print("\n--- DFS Graph Traversal (Directed) ---\n")


class DirectedGraph:
    def __init__(self, labels):
        """Initialisiert einen gerichteten Graphen."""
        self.labels = labels
        self.num_vertices = len(labels)
        self.adj_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]

    def label_to_index(self, label):
        if label not in self.labels:
            raise ValueError(f"Label {label} nicht im Graphen gefunden.")
        return self.labels.index(label)

    def add_edge(self, label_from, label_to, weight=1):
        """Fügt eine gerichtete Kante hinzu (nur eine Richtung)."""
        u = self.label_to_index(label_from)
        v = self.label_to_index(label_to)
        self.adj_matrix[u][v] = weight

    def dfs(self, start_label):
        """DFS für gerichteten Graphen (identisch mit ungerichtet)."""
        visited = set()

        def dfs_helper(label):
            print(label)
            visited.add(label)
            current_index = self.label_to_index(label)

            for neighbor_index, is_connected in enumerate(
                self.adj_matrix[current_index]
            ):
                neighbor_label = self.labels[neighbor_index]
                if is_connected and neighbor_label not in visited:
                    dfs_helper(neighbor_label)

        dfs_helper(start_label)


# Beispiel
labels = ["A", "B", "C", "D"]
graph = DirectedGraph(labels)

# Gerichtete Kanten
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")
graph.add_edge("D", "A")  # Pfeil zeigt zu A, nicht von A weg!

print("DFS-Traversierung ab Knoten A:")
graph.dfs("A")
# Ausgabe: A → B → C
# D wird NICHT besucht, da kein Pfeil von A zu D führt

print("\nDFS-Traversierung ab Knoten D:")
graph.dfs("D")
# Ausgabe: D → A → B → C
# Von D aus können wir A erreichen, und von dort aus B und C

# -----------------------------------------------------------------------------------------

print("\n--- BFS Graph Traversal (Directed) ---\n")

from collections import deque


class DirectedGraph:
    def __init__(self, labels):
        """Initialisiert einen gerichteten Graphen."""
        self.labels = labels
        self.num_vertices = len(labels)
        self.adj_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]

    def label_to_index(self, label):
        if label not in self.labels:
            raise ValueError(f"Label {label} nicht im Graphen gefunden.")
        return self.labels.index(label)

    def add_edge(self, label_from, label_to, weight=1):
        """Fügt eine gerichtete Kante hinzu."""
        u = self.label_to_index(label_from)
        v = self.label_to_index(label_to)
        self.adj_matrix[u][v] = weight

    def bfs(self, start_label):
        """BFS für gerichteten Graphen (identisch mit ungerichtet)."""
        visited = set()
        queue = deque()

        queue.append(start_label)
        visited.add(start_label)

        while queue:
            current_label = queue.popleft()
            print(current_label)

            current_index = self.label_to_index(current_label)

            for neighbor_index, is_connected in enumerate(
                self.adj_matrix[current_index]
            ):
                neighbor_label = self.labels[neighbor_index]
                if is_connected and neighbor_label not in visited:
                    queue.append(neighbor_label)
                    visited.add(neighbor_label)


# Beispiel
labels = ["A", "B", "C", "D"]
graph = DirectedGraph(labels)

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")
graph.add_edge("D", "A")

print("BFS-Traversierung ab Knoten A:")
graph.bfs("A")
# Ausgabe: A → B → C (Ebene 0: A, Ebene 1: B, C)
