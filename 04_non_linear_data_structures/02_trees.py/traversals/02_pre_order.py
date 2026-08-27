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

    def pre_order_traversal(self, start_node, visit_list):
        """
        Pre-Order: Wurzel → Links → Rechts
        Reihenfolge: Besuche aktuellen Knoten ZUERST, dann rekursiv die Kinder
        """
        if start_node is None:
            return

        # 1) Aktuellen Knoten besuchen
        visit_list.append(start_node.value)

        # 2) Linken Teilbaum durchlaufen
        self.pre_order_traversal(start_node.left, visit_list)

        # 3) Rechten Teilbaum durchlaufen
        self.pre_order_traversal(start_node.right, visit_list)


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

# Test der Pre-Order-Traversierung
visit_order = []
bt.pre_order_traversal(bt.root, visit_order)
print("Pre-Order Traversierung (DFS):", visit_order)
# Ausgabe: ['R', 'A', 'C', 'D', 'B', 'E', 'F', 'G']
