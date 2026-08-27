from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert_left(self, current_node, new_value):
        new_node = TreeNode(new_value)
        if current_node.left is None:
            current_node.left = new_node
        else:
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, new_value):
        new_node = TreeNode(new_value)
        if current_node.right is None:
            current_node.right = new_node
        else:
            new_node.right = current_node.right
            current_node.right = new_node

    def level_order_traversal(self, start_node):
        """
        Level-Order / BFS: Alle Knoten auf einer Ebene besuchen, bevor ich zur nächsten Ebene gehe
        Implementierung: Queue (FIFO)
        """
        if start_node is None:
            return []

        visit_list = []
        queue = deque([start_node])  # Queue mit der Wurzel initialisieren

        while queue:
            # Vordersten Knoten aus der Queue entfernen (FIFO)
            current = queue.popleft()
            visit_list.append(current.value)

            # Linkes Kind zur Queue hinzufügen
            if current.left:
                queue.append(current.left)

            # Rechtes Kind zur Queue hinzufügen
            if current.right:
                queue.append(current.right)

        return visit_list


# -- Baum aufbauen --
#      R
#     / \
#    A   B
#   / \ / \
#  C  D E  F
#         /
#        G

bt = BinaryTree("R")
bt.insert_left(bt.root, "A")
bt.insert_right(bt.root, "B")

nodeA = bt.root.left
nodeB = bt.root.right

bt.insert_left(nodeA, "C")
bt.insert_right(nodeA, "D")
bt.insert_left(nodeB, "E")
bt.insert_right(nodeB, "F")

nodeF = nodeB.right
bt.insert_left(nodeF, "G")

# Test der Level-Order-Traversierung (BFS)
visit_order = bt.level_order_traversal(bt.root)
print("Level-Order Traversierung (BFS):", visit_order)
# Ausgabe: ['R', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
# Beachte: Besucht Ebene für Ebene (R), dann (A, B), dann (C, D, E, F), dann (G)
