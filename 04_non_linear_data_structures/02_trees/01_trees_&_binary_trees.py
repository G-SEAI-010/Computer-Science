# ============================================================
# ABSCHNITT 1: BEISPIELE ZUR HÖHENBERECHNUNG
# ============================================================

# Höhe = Anzahl der KANTEN (nicht Knoten) vom Root-Knoten zu seinem tiefsten Blatt.

# Leerer Baum (None): Höhe = -1
# Blattknoten (keine Kinder): Höhe = 0
# Knoten mit Kindern: Höhe = 1 + max(höhe_links, höhe_rechts)

# Beispiel 1: Einfacher Baum
#       A
#      / \
#     B   C
#
# Von unten nach oben (bottom-up) berechnet:
# B ist ein Blatt → Höhe = 0
# C ist ein Blatt → Höhe = 0
# A hat Kinder → Höhe = 1 + max(0, 0) = 1

# Beispiel 2: Tieferer Baum
#       A
#      / \
#     B   C
#    / \  /
#   D  E F
#  /
# G
#
# Von unten nach oben (bottom-up) berechnet:
# G ist ein Blatt → Höhe = 0
# E ist ein Blatt → Höhe = 0
# F ist ein Blatt → Höhe = 0
# D hat das linke Kind G → Höhe = 1 + max(0, -1) = 1
# B hat die Kinder D, E → Höhe = 1 + max(1, 0) = 2
# C hat das linke Kind F → Höhe = 1 + max(0, -1) = 1
# A hat die Kinder B, C → Höhe = 1 + max(2, 1) = 3

# ============================================================
# ABSCHNITT 2: BEISPIELE FÜR BAUMARTEN
# ============================================================

# Allgemeiner Baum - Tree - (beliebige Anzahl von Kindern)
#         A
#       / | \
#      B  C  D
#     /|  |
#    E F  G

# Binärbaum - Binary Tree -  (maximal 2 Kinder)
#       A
#      / \
#     B   C
#    / \
#   D   E

# Binärer Suchbaum - Binary Search Tree - (BST) - sortierte Reihenfolge
#       5
#      / \
#     3   8
#    / \   \
#   1   4   9


# ==========================================================================
# ABSCHNITT 3: KLASSEN FÜR BAUMKNOTEN (Tree Nodes) & BINÄRBAUM (Binary Tree)
# ==========================================================================


class TreeNode:
    """Repräsentiert einen einzelnen Knoten in einem Binärbaum."""

    def __init__(self, value):
        self.value = value
        self.left = None  # Zeiger auf das linke Kind
        self.right = None  # Zeiger auf das rechte Kind

    def __repr__(self):
        """String-Repräsentation für einfaches Debugging in der Konsole."""
        return f"TreeNode({self.value})"


class BinaryTree:
    """Repräsentiert den gesamten Binärbaum."""

    def __init__(self, root_value):
        # Der Baum startet immer mit einem Wurzelknoten (Root)
        self.root = TreeNode(root_value)

    def __repr__(self):
        """Gibt den Wurzelwert aus, wenn der Baum gedruckt wird."""
        return f"BinaryTree(root={self.root.value})"

    def __len__(self):
        """Dunder-Methode, die es erlaubt len(tree) aufzurufen, um alle Knoten zu zählen."""
        return self.count_nodes()

    def insert_left(self, current_node, new_value):
        """Fügt einen neuen Knoten als linkes Kind von current_node ein."""
        new_node = TreeNode(new_value)

        if current_node.left is None:
            # Wenn noch kein linkes Kind existiert, hängen wir das neue einfach an
            current_node.left = new_node
        else:
            # Wenn schon ein linkes Kind existiert, schieben wir es eine Ebene nach unten!
            # Das neue Element nimmt den direkten Platz ein, das alte wird zum Kind des neuen Elements.
            new_node.left = current_node.left
            current_node.left = new_node

        return new_node

    def insert_right(self, current_node, new_value):
        """Fügt einen neuen Knoten als rechtes Kind von current_node ein."""
        new_node = TreeNode(new_value)

        if current_node.right is None:
            current_node.right = new_node
        else:
            # Auch hier: Ein bestehendes rechtes Kind wird eine Ebene nach unten geschoben
            new_node.right = current_node.right
            current_node.right = new_node

        return new_node

    # --- HÖHE BERECHNEN (HEIGHT) ---
    def height(self):
        """Berechnet die Höhe des gesamten Baums (ausgehend von der Wurzel)."""
        return self._height(self.root)

    def _height(self, node):
        """Private, rekursive Hilfsfunktion zur Höhenberechnung."""
        if node is None:
            return -1  # Basisfall: Ein leerer Zweig hat die Höhe -1

        # Addiere 1 für die aktuelle Kante und nimm das Maximum der beiden Zweige darunter
        return 1 + max(self._height(node.left), self._height(node.right))

    # --- KNOTEN ZÄHLEN (COUNT NODES) ---
    def count_nodes(self):
        """Zählt die Gesamtzahl aller Knoten im Baum."""
        return self._count_nodes(self.root)

    def _count_nodes(self, node):
        """Private, rekursive Hilfsfunktion zum Zählen der Knoten."""
        if node is None:
            return 0  # Basisfall: Wenn kein Knoten da ist, zähle 0

        # Zähle den aktuellen Knoten (1) PLUS alle Knoten links PLUS alle Knoten rechts
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    # --- BLÄTTER ZÄHLEN (COUNT LEAVES) ---
    def count_leaves(self):
        """Zählt nur die Blattknoten (Knoten, die keine Kinder haben)."""
        return self._count_leaves(self.root)

    def _count_leaves(self, node):
        """Private, rekursive Hilfsfunktion zum Zählen der Blätter."""
        if node is None:
            return 0

        # Wenn ein Knoten weder linke noch rechte Kinder hat, ist er ein Blatt! Zähle ihn (1).
        if node.left is None and node.right is None:
            return 1

        # Sonst: Durchsuche weiter die Zweige nach unten
        return self._count_leaves(node.left) + self._count_leaves(node.right)


# ============================================================
# BEISPIEL-CODE ZUM TESTEN
# ============================================================

# -- Wir bauen diesen Baum auf --
#      R
#     / \
#    A   B
#   / \ / \
#  C  D E  F
#         /
#        G

# Erstelle den Baum mit der Wurzel 'R'
bt = BinaryTree("R")

# Füge Kinder zur Wurzel hinzu
node_a = bt.insert_left(bt.root, "A")
node_b = bt.insert_right(bt.root, "B")

# Füge Kinder zu A hinzu
bt.insert_left(node_a, "C")
bt.insert_right(node_a, "D")

# Füge Kinder zu B hinzu
bt.insert_left(node_b, "E")
node_f = bt.insert_right(node_b, "F")

# Füge ein Kind zu F hinzu
bt.insert_left(node_f, "G")

# Test: Greife manuell auf Knoten 'E' zu (Wurzel -> rechts -> links)
print("Zugriff auf E:", bt.root.right.left.value)  # Output: E
print("Baum-Objekt:", bt)  # Output: BinaryTree(root=R)

# Teste die Baum-Eigenschaften
print(f"Baum Höhe: {bt.height()}")  # Output: 3
print(f"Anzahl Knoten: {len(bt)}")  # Output: 7
print(f"Blattknoten: {bt.count_leaves()}")  # Output: 4 (Das sind C, D, E, G)
