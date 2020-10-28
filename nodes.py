class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    final = []
    nodes = [node]
    while nodes:
        temp = nodes.pop(0)
        if temp != None:
            nodes += [temp.left, temp.right]
            final.append(temp.value)
    print(final)


tree_by_levels(None)
tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(
    Node(None, None, 5), Node(None, None, 6), 3), 1))
