class AvlNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # Höhe des Teilbaums speichern


class AvlTree:
    def __init__(self):
        self.root = None

    # ================== HILFSMETHODEN ================== #

    def _get_height(self, node):
        """Gibt die Höhe eines Knotens zurück, 0 wenn None."""
        if node is None:
            return 0
        return node.height

    def _update_height(self, node):
        """
        Aktualisiert die Höhe eines Knotens basierend auf seinen Kindern.
        Höhe = 1 + max(Höhe_links, Höhe_rechts)
        """
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _get_balance(self, node):
        """
        Berechnet den Balance-Faktor eines Knotens.
        BF = Höhe(rechts) - Höhe(links)

        BF = -2 oder +2 → unbalanciert und muss rotiert werden
        """
        if node is None:
            return 0
        return self._get_height(node.right) - self._get_height(node.left)

    def _rotate_left(self, z):
        """
        Linksrotation: Korrektur für Rechtslastigkeit (RR/RL-Fälle)
        
        Vorher:                Nachher:
             z                     y
            / \                   / \
          T1   y                 z  T3
              / \               / \
            T2  T3            T1  T2
        """
        y = z.right
        T2 = y.left

        # Rotation durchführen
        y.left = z
        z.right = T2

        # Höhen aktualisieren (zuerst die unteren, dann nach oben)
        self._update_height(z)
        self._update_height(y)

        # Neue Wurzel zurückgeben
        return y

    def _rotate_right(self, z):
        """
        Rechtsrotation: Korrektur für Linkslastigkeit (LL/LR-Fälle)
        
        Vorher:                Nachher:
             z                     y
            / \                   / \
           y  T3                T1   z
          / \                       / \
        T1  T2                     T2  T3
        """
        y = z.left
        T2 = y.right

        # Rotation durchführen
        y.right = z
        z.left = T2

        # Höhen aktualisieren
        self._update_height(z)
        self._update_height(y)

        # Neue Wurzel zurückgeben
        return y

    def _rebalance(self, node, inserted_value=None):
        """
        Prüft den Balance-Faktor und führt notwendige Rotationen durch.
        inserted_value hilft bei der Erkennung des richtigen Rotationstyps.
        """
        balance = self._get_balance(node)

        # LL: Linkslastig, linkes Kind auch linkslastig
        if balance < -1 and inserted_value < node.left.value:
            return self._rotate_right(node)

        # RR: Rechtslastig, rechtes Kind auch rechtslastig
        if balance > 1 and inserted_value > node.right.value:
            return self._rotate_left(node)

        # LR: Linkslastig, aber linkes Kind ist rechtslastig
        if balance < -1 and inserted_value > node.left.value:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # RL: Rechtslastig, aber rechtes Kind ist linkslastig
        if balance > 1 and inserted_value < node.right.value:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    # ================== EINFÜGEN (INSERT) ================== #

    def _insert_recursive(self, node, value):
        """Rekursive Einfügungsfunktion mit Balancierung."""
        # Standard BST Einfügung
        if node is None:
            return AvlNode(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)

        # Höhe aktualisieren und balancieren
        self._update_height(node)
        return self._rebalance(node, inserted_value=value)

    def insert(self, value):
        """Einfügen eines Wertes mit automatischer Balancierung."""
        self.root = self._insert_recursive(self.root, value)

    # ================== LÖSCHEN (DELETE) ================== #

    def _find_min(self, node):
        """
        Findet den kleinsten Knoten aus dem Teilbaum.
        Nutzen wir beim Löschen von Knoten mit zwei Kindern.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _delete_recursive(self, node, value):
        """Rekursive Löschfunktion mit Balancierung."""
        if node is None:
            return node

        # Standard BST Löschansatz
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Knoten gefunden
            # Fall 1: Blattknoten (keine Kinder)
            if node.left is None and node.right is None:
                node = None
            # Fall 2: Ein Kind
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            # Fall 3: Zwei Kinder
            else:
                # Finde In-Order-Nachfolger (kleinster Wert im rechten Teilbaum)
                successor = self._find_min(node.right)
                node.value = successor.value
                # Lösche den Nachfolger
                node.right = self._delete_recursive(node.right, successor.value)

        # Wenn der Knoten None ist, zurückgeben
        if node is None:
            return node

        # Höhe aktualisieren und balancieren
        self._update_height(node)
        return self._rebalance(node)

    def delete(self, value):
        """Löschen eines Wertes mit automatischer Balancierung."""
        self.root = self._delete_recursive(self.root, value)

    # ================== SUCHEN (SEARCH) ================== #

    def search(self, value):
        """
        Sucht nach 'value' beginnend bei der Wurzel.
        Gibt True zurück, falls gefunden, andernfalls False.
        """
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    # ================== TRAVERSIERUNG ================== #

    def in_order_traversal(self, node, result):
        """In-Order Traversierung (sortiert)."""
        if node is None:
            return
        self.in_order_traversal(node.left, result)
        result.append(node.value)
        self.in_order_traversal(node.right, result)

    # ================== AUSGABE (PRINTING) ================== #

    def print_tree(self, node, level=0, branch="root"):
        """
        Gibt den Baum seitwärts aus mit Balance-Faktor und Höhe.

        ↗ wenn dieser Knoten ein rechtes Kind ist
        ↘ wenn dieser Knoten ein linkes Kind ist

        Jede Ebene wird weiter eingerückt, um die Hierarchie zu zeigen.
        """
        if node is None:
            return

        # Rechter Teilbaum
        self.print_tree(node.right, level + 1, "right")

        # Einrückung aufbauen
        indent = "    " * level

        # Aktuellen Knoten beschriften
        bf = self._get_balance(node)
        h = self._get_height(node)

        if branch == "root":
            print(f"{indent}{node.value} (BF={bf:+d}, H={h})")
        elif branch == "right":
            print(f"{indent}↗ {node.value} (BF={bf:+d}, H={h})")
        else:  # branch == "left"
            print(f"{indent}↘ {node.value} (BF={bf:+d}, H={h})")

        # Linker Teilbaum
        self.print_tree(node.left, level + 1, "left")


# ================== BEISPIEL ================== #

print("=== AVL-Baum Demonstration ===\n")

avl = AvlTree()

# Einfügungen
values = [10, 20, 5, 4, 15, 25, 2, 7]
print(f"Einfügen von: {values}")
for val in values:
    avl.insert(val)

# In-Order (sollte sortiert sein)
inorder_vals = []
avl.in_order_traversal(avl.root, inorder_vals)
print(f"In-Order vor Löschvorgängen: {inorder_vals}")

print("\n--- Visueller Baum (vor Löschvorgängen) ---")
avl.print_tree(avl.root)

# Löschen
print("\n=== Lösche 15 und 4 ===")
avl.delete(15)
avl.delete(4)

# Suchen
print(f"\nSuche nach 5: {avl.search(5)}")
print(f"Suche nach 4: {avl.search(4)}")

# In-Order nach Löschen
inorder_vals = []
avl.in_order_traversal(avl.root, inorder_vals)
print(f"\nIn-Order nach Löschvorgängen: {inorder_vals}")

print("\n--- Visueller Baum (nach Löschvorgängen) ---")
avl.print_tree(avl.root)
