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

    def post_order_traversal(self, start_node, visit_list):
        """
        Post-Order: Links → Rechts → Wurzel
        Reihenfolge: Durchlaufe beide Teilbäume, DANN besuche den Knoten
        """
        if start_node is None:
            return

        # 1) Linken Teilbaum durchlaufen
        self.post_order_traversal(start_node.left, visit_list)

        # 2) Rechten Teilbaum durchlaufen
        self.post_order_traversal(start_node.right, visit_list)

        # 3) Aktuellen Knoten besuchen
        visit_list.append(start_node.value)


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

# Test der Post-Order-Traversierung
visit_order = []
bt.post_order_traversal(bt.root, visit_order)
print("Post-Order Traversierung (DFS):", visit_order)
# Ausgabe: ['C', 'D', 'A', 'E', 'G', 'F', 'B', 'R']
