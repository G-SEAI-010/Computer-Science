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

    def in_order_traversal(self, start_node, visit_list):
        """
        In-Order: Links → Wurzel → Rechts
        Reihenfolge: Durchlaufe linken Teilbaum, besuche DANN den Knoten, dann rechts
        WICHTIG: Bei binären Suchbäumen erzeugt dies sortierte Ausgabe!
        """
        if start_node is None:
            return

        # 1) Linken Teilbaum durchlaufen
        self.in_order_traversal(start_node.left, visit_list)

        # 2) Aktuellen Knoten besuchen
        visit_list.append(start_node.value)

        # 3) Rechten Teilbaum durchlaufen
        self.in_order_traversal(start_node.right, visit_list)


# -- Baum aufbauen --
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

# Test der In-Order-Traversierung
visit_order = []
bt.in_order_traversal(bt.root, visit_order)
print("In-Order Traversierung (DFS):", visit_order)
# Ausgabe: ['C', 'A', 'D', 'R', 'E', 'B', 'G', 'F']
