# Example tree structure
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# Function to perform depth-first search with alpha-beta pruning


def alpha_beta(node, alpha, beta, maximizing_player):
    if node is None:
        return 0

    if not node.children:  # Leaf node
        return node.value

    if maximizing_player:
        value = float("-inf")
        for child in node.children:
            value = max(value, alpha_beta(child, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break  # Beta cutoff
        return value
    else:
        value = float("inf")
        for child in node.children:
            value = min(value, alpha_beta(child, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break  # Alpha cutoff
        return value


# Example tree
root = Node(3)
root.add_child(Node(5))
root.add_child(Node(6))
root.add_child(Node(9))

# First level children
root.children[0].add_child(Node(2))
root.children[0].add_child(Node(8))
root.children[0].add_child(Node(1))

root.children[1].add_child(Node(12))
root.children[1].add_child(Node(14))

root.children[2].add_child(Node(3))
root.children[2].add_child(Node(7))

# Second level children
root.children[0].children[0].add_child(Node(10))
root.children[0].children[0].add_child(Node(6))


def print_tree(node, prefix="", is_tail=True):
    print(prefix + ("└── " if is_tail else "├── ") + str(node.value))
    children_count = len(node.children)
    for i, child in enumerate(node.children):
        is_last_child = (i == children_count - 1)
        print_tree(child, prefix +
                   ("    " if is_tail else "│   "), is_last_child)


print("Example Tree:")
print_tree(root)

result = alpha_beta(root, float("-inf"), float("inf"), True)
print("Optimal value:", result)
