print("--------------- Undirected Graph ---------------\n")


class UndirectedGraph:
    def __init__(self, labels):
        """
        Initialisiert einen ungerichteten Graphen mit den bereitgestellten Knoten-Labels.

        In einem UNGERICHTETEN Graphen funktionieren Kanten in beide Richtungen
        - wie eine Zweibahnstraße.
        Wenn es eine Kante von A nach B gibt, kann man auch von B nach A reisen.

        Args:
            labels: Liste der Knotennamen, z. B. ["A", "B", "C", "D"]
        """
        self.labels = labels
        self.num_vertices = len(labels)
        # n×n-Matrix erstellen, initialisiert mit 0 (keine Kanten)
        self.adj_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def label_to_index(self, label):
        """Konvertiert ein Knoten-Label (wie 'A') in seinen Index (wie 0)."""
        if label not in self.labels:
            raise ValueError(f"Label {label} nicht im Graphen gefunden.")
        return self.labels.index(label)

    def add_edge(self, label1, label2, weight=1):
        """
        Fügt eine Kante zwischen zwei Knoten hinzu.

        KERNKONZEPT: In ungerichteten Graphen aktualisieren wir BEIDE Richtungen!
        """
        u = self.label_to_index(label1)
        v = self.label_to_index(label2)

        # WICHTIG: Für ungerichtete Graphen beide Richtungen aktualisieren
        self.adj_matrix[u][v] = weight  # A → B
        self.adj_matrix[v][u] = weight  # B → A (symmetrisch)

    def remove_edge(self, label1, label2):
        """Entfernt eine Kante zwischen zwei Knoten."""
        u = self.label_to_index(label1)
        v = self.label_to_index(label2)

        # Beide Richtungen entfernen
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0

    def get_neighbors(self, label):
        """Gibt alle direkten Nachbarn eines Knotens zurück."""
        i = self.label_to_index(label)
        return [
            self.labels[j]
            for j in range(self.num_vertices)
            if self.adj_matrix[i][j] != 0
        ]

    def edge_exists(self, label1, label2):
        """Prüft, ob eine Kante zwischen zwei Knoten existiert."""
        u = self.label_to_index(label1)
        v = self.label_to_index(label2)
        return self.adj_matrix[u][v] != 0

    def print_matrix(self):
        """Gibt die Adjazenzmatrix aus."""
        # Kopfzeile mit Knoten-Labels
        header = "   " + "  ".join(self.labels)
        print(header)
        # Jede Zeile mit ihrem Label
        for i, row in enumerate(self.adj_matrix):
            row_str = "  ".join(str(x) for x in row)
            print(f"{self.labels[i]}  {row_str}")


# Beispiel
labels = ["A", "B", "C", "D"]
graph = UndirectedGraph(labels)

# Kanten hinzufügen
graph.add_edge("A", "B", 1)
graph.add_edge("A", "C", 2)
graph.add_edge("B", "C", 3)
graph.add_edge("C", "D", 4)

print("Ungerichteter Graph - Adjazenzmatrix:")
graph.print_matrix()

print(f"\nNachbarn von A: {graph.get_neighbors('A')}")
print(f"Kante von A zu B existiert: {graph.edge_exists('A', 'B')}")
print(f"Kante von A zu D existiert: {graph.edge_exists('A', 'D')}")

print("\n--------------- Directed Graph ---------------\n")


class DirectedGraph:
    def __init__(self, labels):
        """
        Initialisiert einen gerichteten Graphen mit den bereitgestellten Knoten-Labels.

        In einem GERICHTETEN Graphen sind Kanten Einbahnstraßen.
        Eine Kante von A nach B bedeutet NICHT, dass man von B nach A gehen kann.
        """
        self.labels = labels
        self.num_vertices = len(labels)
        self.adj_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]

    def label_to_index(self, label):
        """Konvertiert ein Knoten-Label in seinen Matrix-Index."""
        if label not in self.labels:
            raise ValueError(f"Label {label} nicht im Graphen gefunden.")
        return self.labels.index(label)

    def add_edge(self, label_from, label_to, weight=1):
        """
        Fügt eine GERICHTETE Kante von einem Knoten zu einem anderen hinzu.

        HAUPTUNTERSCHIED: Wir aktualisieren nur EINE Richtung!
        """
        u = self.label_to_index(label_from)
        v = self.label_to_index(label_to)

        # WICHTIG: Bei gerichteten Graphen nur EINE Richtung aktualisieren
        self.adj_matrix[u][v] = weight  # nur A → B

    def remove_edge(self, label_from, label_to):
        """Entfernt eine GERICHTETE Kante."""
        u = self.label_to_index(label_from)
        v = self.label_to_index(label_to)

        # Nur die angegebene Richtung entfernen
        self.adj_matrix[u][v] = 0

    def get_outgoing(self, label):
        """Gibt alle ausgehenden Nachbarn eines Knotens zurück (A → ?)."""
        i = self.label_to_index(label)
        return [
            self.labels[j]
            for j in range(self.num_vertices)
            if self.adj_matrix[i][j] != 0
        ]

    def get_incoming(self, label):
        """Gibt alle eingehenden Nachbarn eines Knotens zurück (? → A)."""
        j = self.label_to_index(label)
        return [
            self.labels[i]
            for i in range(self.num_vertices)
            if self.adj_matrix[i][j] != 0
        ]

    def print_matrix(self):
        """Gibt die Adjazenzmatrix aus."""
        # Spaltenüberschriften
        header = "    " + "  ".join(self.labels)
        print(header)
        # Jede Zeile mit ihrem Label
        for i, row in enumerate(self.adj_matrix):
            row_str = "  ".join(str(x) for x in row)
            print(f"{self.labels[i]}   {row_str}")


# Beispiel
labels = ["A", "B", "C", "D"]
graph = DirectedGraph(labels)

# Gerichtete Kanten hinzufügen
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")
graph.add_edge("C", "D")
graph.add_edge("D", "A")  # Erzeugt einen Zyklus!

print("Gerichteter Graph - Adjazenzmatrix:")
graph.print_matrix()

print(f"\nAusgehende von A: {graph.get_outgoing('A')}")
print(f"Eingehende zu A: {graph.get_incoming('A')}")
print(f"Ausgehende von D: {graph.get_outgoing('D')}")

print("\n--------------- Adjazenzliste ---------------\n")


class GraphAdjacencyList:
    def __init__(self):
        """Initialisiert einen Graphen mit Adjazenzliste (als Dictionary)."""
        self.graph = {}

    def add_vertex(self, vertex):
        """Fügt einen Knoten hinzu."""
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v, weight=1, directed=False):
        """
        Fügt eine Kante hinzu.

        Args:
            u: Startknoten
            v: Zielknoten
            weight: Kantengewicht
            directed: True = gerichtet, False = ungerichtet
        """
        # Sicherstelle, dass Knoten existieren
        self.add_vertex(u)
        self.add_vertex(v)

        # Füge Kante hinzu
        self.graph[u].append((v, weight))

        # Für ungerichtete Graphen: Füge auch die Rückwärtskante hinzu
        if not directed:
            self.graph[v].append((u, weight))

    def remove_edge(self, u, v, directed=False):
        """Entfernt eine Kante."""
        if u in self.graph:
            self.graph[u] = [
                (neighbor, w) for neighbor, w in self.graph[u] if neighbor != v
            ]

        if not directed and v in self.graph:
            self.graph[v] = [
                (neighbor, w) for neighbor, w in self.graph[v] if neighbor != u
            ]

    def get_neighbors(self, vertex):
        """Gibt alle Nachbarn eines Knotens zurück."""
        if vertex in self.graph:
            return [neighbor for neighbor, _ in self.graph[vertex]]
        return []

    def print_graph(self):
        """Gibt die Adjazenzliste aus."""
        for vertex in self.graph:
            neighbors_str = ", ".join(f"{v}({w})" for v, w in self.graph[vertex])
            print(f"{vertex}: [{neighbors_str}]")


# Beispiel: Ungerichteter Graph
print("=== Ungerichteter Graph (Adjazenzliste) ===")
graph = GraphAdjacencyList()

graph.add_edge("A", "B", 1)
graph.add_edge("B", "C", 2)
graph.add_edge("C", "D", 3)
graph.add_edge("A", "D", 4)

graph.print_graph()

print(f"\nNachbarn von A: {graph.get_neighbors('A')}")
print(f"Nachbarn von B: {graph.get_neighbors('B')}")

# Beispiel: Gerichteter Graph
print("\n=== Gerichteter Graph (Adjazenzliste) ===")
digraph = GraphAdjacencyList()

digraph.add_edge("A", "B", directed=True)
digraph.add_edge("B", "C", directed=True)
digraph.add_edge("C", "D", directed=True)
digraph.add_edge("D", "A", directed=True)

digraph.print_graph()
