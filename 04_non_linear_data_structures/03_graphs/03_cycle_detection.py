print("\n--- DFS Cycle Detection (Undirected) ---\n")


class UndirectedGraph:
    def __init__(self, labels):
        self.labels = labels
        self.num_vertices = len(labels)
        self.adj_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def label_to_index(self, label):
        if label not in self.labels:
            raise ValueError(f"Label {label} nicht im Graphen gefunden.")
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

    def detect_cycle_dfs(self):
        """
        Erkennt mithilfe von DFS, ob es einen Zyklus im ungerichteten Graphen gibt.

        In einem ungerichteten Graphen existiert ein Zyklus, wenn wir auf einen
        besuchten Knoten stoßen, der NICHT der direkte Elternknoten ist.

        Returns:
            True wenn Zyklus, False sonst
        """
        visited = [False] * self.num_vertices

        def dfs(curr, parent):
            """
            DFS-Hilfsfunktion zur Zyklenerkennung.

            Args:
                curr: Index des aktuellen Knotens
                parent: Index des Elternknotens (-1 wenn Startknoten)

            Returns:
                True wenn Zyklus erkannt, False sonst
            """
            visited[curr] = True

            # Alle Nachbarn erkunden
            for neighbor in range(self.num_vertices):
                if self.adj_matrix[curr][neighbor] != 0:  # Es gibt eine Kante

                    if not visited[neighbor]:
                        # Fall 1: Nachbar nicht besucht → rekursiv erkunden
                        if dfs(neighbor, curr):
                            return True  # Zyklus in Tiefe gefunden

                    elif neighbor != parent:
                        # Fall 2: Nachbar besucht UND nicht Parent
                        # → Zyklus gefunden!
                        #
                        # Warum neighbor != parent?
                        # In ungerichteten Graphen führt jede Kante in beide Richtungen.
                        # Wenn wir von A zu B kamen, gibt es auch B → A.
                        # Ohne diese Prüfung würde jede Kante als Zyklus erkannt!
                        return True

            return False

        # DFS von jedem unbesuchten Knoten starten
        # (Behandelt unzusammenhängende Graphen)
        for vertex in range(self.num_vertices):
            if not visited[vertex]:
                if dfs(vertex, -1):
                    return True

        return False


# Beispiel
labels = ["A", "B", "C", "D"]
graph = UndirectedGraph(labels)

# Kanten hinzufügen
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("A", "D")
graph.add_edge("B", "C")  # Erzeugt einen Zyklus: A-B-C-A

print("Adjazenzmatrix des ungerichteten Graphen:")
graph.print_matrix()

if graph.detect_cycle_dfs():
    print("\n✓ Zyklus im ungerichteten Graphen erkannt!")
else:
    print("\n✗ Kein Zyklus im ungerichteten Graphen gefunden.")

# -----------------------------------------------------------------------------------------

print("\n--- DFS Cycle Detection (Directed) ---\n")


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

    def detect_cycle_dfs(self):
        """
        Erkennt mithilfe von DFS, ob es einen Zyklus im gerichteten Graphen gibt.

        In einem gerichteten Graphen existiert ein Zyklus, wenn wir auf einen Knoten
        stoßen, der sich aktuell im Rekursions-Stack (aktiver Pfad) befindet.
        Das nennt man eine "Rückwärtskante" (back edge).

        KRITISCH: Wir benötigen ZWEI Arrays:
        - visited: alle jemals gesehenen Knoten
        - rec_stack: nur Knoten im AKTUELLEN Pfad

        Returns:
            True wenn Zyklus, False sonst
        """
        visited = [False] * self.num_vertices
        rec_stack = [False] * self.num_vertices

        def dfs(curr):
            """
            DFS-Hilfsfunktion zur Zyklenerkennung.

            Args:
                curr: Index des aktuellen Knotens

            Returns:
                True wenn Zyklus erkannt, False sonst
            """
            visited[curr] = True
            rec_stack[curr] = True  # Zum aktuellen Pfad hinzufügen

            # Alle Nachbarn erkunden
            for neighbor in range(self.num_vertices):
                if self.adj_matrix[curr][neighbor] != 0:  # Es gibt eine Kante

                    if not visited[neighbor]:
                        # Fall 1: Nachbar nicht besucht → rekursiv erkunden
                        if dfs(neighbor):
                            return True

                    elif rec_stack[neighbor]:
                        # Fall 2: Nachbar im aktuellen Pfad
                        # → Rückwärtskante = Zyklus!
                        #
                        # Warum rec_stack statt visited?
                        # visited sagt: "wurde irgendwann besucht"
                        # rec_stack sagt: "ist noch im aktuellen Pfad"
                        #
                        # Beispiel:
                        #   A → B → D
                        #   A → C
                        # Wenn wir C → B sehen:
                        #   visited[B] = True (wurde besucht)
                        #   rec_stack[B] = False (nicht im aktuellen Pfad!)
                        #   Keine Rückwärtskante → Kein Zyklus
                        #
                        # Aber wenn C → A:
                        #   visited[A] = True
                        #   rec_stack[A] = True (A ist noch aktiv!)
                        #   Rückwärtskante erkannt → Zyklus!
                        return True

            # Aus dem aktuellen Pfad entfernen (Backtrack)
            # KRITISCH: Andernfalls gibt es falsche Positive!
            rec_stack[curr] = False
            return False

        # DFS von jedem unbesuchten Knoten starten
        for vertex in range(self.num_vertices):
            if not visited[vertex]:
                if dfs(vertex):
                    return True

        return False


# Beispiel
labels = ["A", "B", "C", "D"]
graph = DirectedGraph(labels)

# Gerichtete Kanten hinzufügen
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")
graph.add_edge("C", "D")
graph.add_edge("D", "A")  # Erzeugt einen Zyklus: A→B→C→D→A

print("Adjazenzmatrix des gerichteten Graphen:")
graph.print_matrix()

if graph.detect_cycle_dfs():
    print("\n✓ Zyklus im gerichteten Graphen erkannt!")
else:
    print("\n✗ Kein Zyklus im gerichteten Graphen gefunden.")
