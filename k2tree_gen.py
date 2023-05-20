import numpy as np

# Node class for k2-tree
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    # used for printing the tree
    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret

# Generate a k2-tree from the adjacency matrix
def k2_tree(matrix, k):
    n = len(matrix)

    matrix_array = np.array(matrix)
    if np.all(matrix_array == 0):
        return Node(0)

    if n == 1:
        return Node(matrix_array[0, 0])

    nodes = []
    size = n // k
    for i in range(k):
        for j in range(k):
            nodes.append(k2_tree(matrix_array[i*size:(i+1)*size, j*size:(j+1)*size].tolist(), k))

    node = Node(any(node.value == 1 for node in nodes))
    node.children = nodes

    return node

def count_nodes(node):
    return 1 + sum(count_nodes(child) for child in node.children)
