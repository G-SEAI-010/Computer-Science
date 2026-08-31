class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, root_value) -> None:
        self.root = Node(root_value)

    def insert(self, value):
        #  startet die Suche nach dem richtigen Platz ab der root
        self._insert_recursively(self.root, value)

    def _insert_recursively(self, curr_node, value):
        # Kernidee des BST: kleinere Werte gehen nach links, größere/gleiche nach rechts.
        # So bleibt der Baum immer sortiert, ohne dass wir ihn extra sortieren müssen.
        if value < curr_node.value:
            if curr_node.left is None:
                # Freie Stelle gefunden -> neue Node einfügen
                curr_node.left = Node(value)
            else:
                # Stelle ist belegt -> eine Ebene tiefer weitersuchen
                self._insert_recursively(curr_node.left, value)
        else:
            if curr_node.right is None:
                curr_node.right = Node(value)
            else:
                self._insert_recursively(curr_node.right, value)

    # Search
    def search(self, value):
        # Iterative Suche: wir laufen ab der Wurzel den Baum entlang,
        # bei jedem Schritt entscheidet der Vergleich, ob wir links oder rechts weitergehen.
        curr = self.root
        while curr is not None:
            if value == curr.value:
                return True
            elif value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        # curr ist None geworden, ohne den Wert zu finden -> Wert existiert nicht im Baum
        return False

    # in-order-traversal
    def in_order_traversal(self, start_node, visit_list):
        if start_node is None:
            return

        # 1) Linken Teilbaum durchlaufen
        self.in_order_traversal(start_node.left, visit_list)

        # 2) Aktuellen Knoten besuchen
        visit_list.append(start_node.value)

        # 3) Rechten Teilbaum durchlaufen
        self.in_order_traversal(start_node.right, visit_list)

    # Delete

    def delete(self, value):
        # Der Baum kann sich durch das Löschen verändern (z.B. die Wurzel wird ersetzt),
        # deshalb überschreiben wir self.root mit dem Ergebnis der rekursiven Löschfunktion.
        self.root = self._delete_recursively(self.root, value)

    def _delete_recursively(self, curr_node, value):

        # Base Case: leerer Teilbaum -> nichts zu tun
        if curr_node is None:
            return None

        # 1. Finde zu löschende Node
        # Wie bei insert/search: über Vergleiche links oder rechts weitersuchen

        if value < curr_node.value:
            curr_node.left = self._delete_recursively(curr_node.left, value)

        elif value > curr_node.value:
            curr_node.right = self._delete_recursively(curr_node.right, value)

        else:
            # 2. Wert gefunden -> Löschen
            # Jetzt gibt es drei mögliche Fälle, je nachdem wie viele Kinder die Node hat

            # 2.a Node hat keine Kinder
            # -> einfach entfernen
            if curr_node.left is None and curr_node.right is None:
                curr_node = None

            # 2.b Node hat ein einzelnes Kind
            # -> Node durch Kind ersetzen (das Kind "rückt nach oben")
            elif curr_node.left is None:
                curr_node = curr_node.right
            elif curr_node.right is None:
                curr_node = curr_node.left

            # 2.c Node hat zwei Kinder
            # -> Richtigen Nachfolger ermitteln:
            # das ist der kleinste Wert im rechten Teilbaum (ganz links unten),
            # denn er ist der nächstgrößere Wert nach curr_node.value
            else:
                successor = curr_node.right
                while successor.left is not None:
                    successor = successor.left

                # Wert des Nachfolgers übernehmen und das Duplikat im rechten Teilbaum löschen
                curr_node.value = successor.value
                curr_node.right = self._delete_recursively(
                    curr_node.right, successor.value
                )

        return curr_node


bst = BinarySearchTree(3)

# print(bst)
bst.insert(1)
bst.insert(2)
bst.insert(5)
bst.insert(4)
bst.insert(6)
bst.insert(12)
bst.insert(42)
bst.insert(17)
bst.insert(15)
bst.insert(16)
# Einfache Binary Search Trees können zu Linked Lists degradieren. Dann verlaufen Suche, Insertion, Deletion nicht mehr logarithmisch, sondern linear!
