# ==========================================
# Ansatz 1: Rekursiv mit Bereichsgrenzen
# ==========================================

"""
Zeitkomplexität: O(n)
- n = Anzahl der Knoten
- Jedes Element im Preorder-Array wird exakt einmal verarbeitet.
- Der Index (idx) zählt von 0 bis n-1 hoch.
- Die Überprüfung der Grenzen (Range-Checks) benötigt O(1).
- Gesamt: O(n)

Speicherkomplexität: O(h)
- h = Höhe des Baums
- Die maximale Tiefe des Rekursions-Stacks entspricht der Baumhöhe.
- Bester Fall (balancierter Baum): h = log(n), also O(log n).
- Schlechtester Fall (Baum ist eine gerade Linie): h = n, also O(n).
- Durchschnittlicher Fall: O(log n).
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bst_from_preorder(preorder):
    if not preorder:
        return None

    def build(min_val, max_val):
        nonlocal idx

        if idx >= len(preorder) or not (min_val < preorder[idx] < max_val):
            return None

        val = preorder[idx]
        node = TreeNode(val)

        idx += 1

        node.left = build(min_val, val)

        node.right = build(val, max_val)

        return node

    idx = 0
    return build(float("-inf"), float("inf"))


def tree_to_list_level_order(root):
    """
    Übersetzt ein Baum-Objekt zurück in eine Liste (Ebene für Ebene, von links nach rechts).
    (Breadth-First Search / BFS)
    """

    if not root:
        return []

    result = []

    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)

            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")

    while result and result[-1] == "null":
        result.pop()

    return result


root1 = bst_from_preorder([8, 5, 1, 7, 10, 12])
print("Beispiel 1 Ausgabe:", tree_to_list_level_order(root1))

root2 = bst_from_preorder([1, 3])
print("Beispiel 2 Ausgabe:", tree_to_list_level_order(root2))


# ==========================================
# Schritt-für-Schritt (Ansatz 1)
# ==========================================
# preorder = [8, 5, 1, 7, 10, 12]
# idx = 0

# Aufruf: build(-∞, +∞)
#   idx=0, val=8, Bereich=(-∞, +∞) ✓
#   Erstelle Knoten(8), idx=1

#   Baue links von 8: build(-∞, 8)
#     idx=1, val=5, Bereich=(-∞, 8) ✓
#     Erstelle Knoten(5), idx=2

#     Baue links von 5: build(-∞, 5)
#       idx=2, val=1, Bereich=(-∞, 5) ✓
#       Erstelle Knoten(1), idx=3

#       Baue links von 1: build(-∞, 1)
#         idx=3, val=7, Bereich=(-∞, 1) ✗ (7 > 1, passt nicht)
#         gibt None zurück

#       Baue rechts von 1: build(1, 5)
#         idx=3, val=7, Bereich=(1, 5) ✗ (7 > 5, passt nicht)
#         gibt None zurück

#       Gibt Knoten(1) zurück

#     Baue rechts von 5: build(5, 8)
#       idx=3, val=7, Bereich=(5, 8) ✓
#       Erstelle Knoten(7), idx=4

#       Baue links von 7: build(5, 7)
#         idx=4, val=10, Bereich=(5, 7) ✗ (10 > 7)
#         gibt None zurück

#       Baue rechts von 7: build(7, 8)
#         idx=4, val=10, Bereich=(7, 8) ✗ (10 > 8)
#         gibt None zurück

#       Gibt Knoten(7) zurück

#     Gibt Knoten(5) mit left=Knoten(1), right=Knoten(7) zurück

#   Baue rechts von 8: build(8, +∞)
#     idx=4, val=10, Bereich=(8, +∞) ✓
#     Erstelle Knoten(10), idx=5

#     Baue links von 10: build(8, 10)
#       idx=5, val=12, Bereich=(8, 10) ✗ (12 > 10)
#       gibt None zurück

#     Baue rechts von 10: build(10, +∞)
#       idx=5, val=12, Bereich=(10, +∞) ✓
#       Erstelle Knoten(12), idx=6

#       Baue links von 12: build(10, 12)
#         idx=6, außerhalb der Index-Grenzen (Ende der Liste)
#         gibt None zurück

#       Baue rechts von 12: build(12, +∞)
#         idx=6, außerhalb der Index-Grenzen
#         gibt None zurück

#       Gibt Knoten(12) zurück

#     Gibt Knoten(10) mit right=Knoten(12) zurück

#   Gibt Knoten(8) mit left=Knoten(5), right=Knoten(10) zurück

# Endgültiger Baum:
#        8
#       / \
#      5   10
#     / \    \
#    1   7   12


# ==========================================
# Ansatz 2: Stack-basiert & iterativ
# ==========================================

"""
Zeitkomplexität: O(n)
- Jedes Element im Array wird exakt einmal verarbeitet: O(n)
- Jedes Element wird maximal einmal auf den Stack gelegt: O(n)
- Jedes Element wird maximal einmal vom Stack genommen (gepoppt): O(n)
- Gesamt: O(n)

Speicherkomplexität: O(h)
- Der Stack speichert die Vorfahren (Ancestors) des aktuellen Knotens.
- Die maximale Größe des Stacks entspricht der Baumhöhe.
- Bester Fall (balanciert): O(log n)
- Schlechtester Fall (Linie): O(n)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bst_from_preorder_iterative(preorder):
    if not preorder:
        return None

    root = TreeNode(preorder[0])

    stack = [root]

    for val in preorder[1:]:
        node = TreeNode(val)

        if val < stack[-1].val:
            stack[-1].left = node

        else:
            parent = None

            while stack and stack[-1].val < val:
                parent = stack.pop()

            parent.right = node

        stack.append(node)

    return root


def tree_to_list_level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")

    while result and result[-1] == "null":
        result.pop()

    return result


print()

root1 = bst_from_preorder_iterative([8, 5, 1, 7, 10, 12])
print("Beispiel 1 Ausgabe:", tree_to_list_level_order(root1))

root2 = bst_from_preorder_iterative([1, 3])
print("Beispiel 2 Ausgabe:", tree_to_list_level_order(root2))

# ==========================================
# Schritt-für-Schritt (Ansatz 2)
# ==========================================
# preorder = [8, 5, 1, 7, 10, 12]

# Schritt 1: root = Knoten(8), stack = [8]

# Schritt 2: val = 5
#   5 < 8, also ist 5 das linke Kind von 8.
#   8.left = Knoten(5)
#   stack = [8, 5]

# Schritt 3: val = 1
#   1 < 5, also ist 1 das linke Kind von 5.
#   5.left = Knoten(1)
#   stack = [8, 5, 1]

# Schritt 4: val = 7
#   7 > 1, pop 1 vom Stack (potenzieller parent = 1)
#   7 > 5, pop 5 vom Stack (potenzieller parent = 5)
#   7 < 8, stopp! (8 bleibt auf dem Stack)
#   5.right = Knoten(7)
#   stack = [8, 7]

# Schritt 5: val = 10
#   10 > 7, pop 7 (parent = 7)
#   10 > 8, pop 8 (parent = 8)
#   Stack ist nun leer, stopp!
#   8.right = Knoten(10)
#   stack = [10]

# Schritt 6: val = 12
#   12 > 10, pop 10 (parent = 10)
#   Stack ist leer, stopp!
#   10.right = Knoten(12)
#   stack = [12]

# Endgültiger Baum:
#        8
#       / \
#      5   10
#     / \    \
#    1   7   12
