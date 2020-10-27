class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    if node == None:
        print(None)
    else:
        lista = []
        if node.value != None:
            lista.append(node.value)
            left = node.left
            right = node.right
        print(lista)


tree_by_levels(None)
tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(
    Node(None, None, 5), Node(None, None, 6), 3), 1))
