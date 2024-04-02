import random
import math


class Node:
    def __init__(self, rem_stones):
        self.rem_stones = rem_stones
        self.children = []
        self.value = 0
        self.level = 0
        self.alpha = float('-inf')
        self.beta = float('inf')

    def addChild(self, child):
        self.children.append(child)

    def setValue(self, value):
        self.value = value

    def setLevel(self, level):
        self.level = level


def dfs(node, level, alpha, beta):
    rem_stones = node.rem_stones
    if rem_stones == 0:
        if level % 2 == 0:
            node.setValue(-1)
        else:
            node.setValue(1)
        return node.value

    if level % 2 == 0:  # Max player's turn
        value = float('-inf')
        for i in range(1, min(rem_stones + 1, 4)):
            new_stones = rem_stones - i
            child = Node(new_stones)
            child.setLevel(level + 1)
            node.addChild(child)
            value = max(value, dfs(child, level + 1, alpha, beta))
            alpha = max(alpha, value)
            if beta <= alpha:
                break  # Beta cutoff
        node.setValue(value)
        return value
    else:  # Min player's turn
        value = float('inf')
        for i in range(1, min(rem_stones + 1, 4)):
            new_stones = rem_stones - i
            child = Node(new_stones)
            child.setLevel(level + 1)
            node.addChild(child)
            value = min(value, dfs(child, level + 1, alpha, beta))
            beta = min(beta, value)
            if beta <= alpha:
                break  # Alpha cutoff
        node.setValue(value)
        return value


n = int(input("Enter Number : "))
root = Node(n)

dfs(root, 0, float('-inf'), float('inf'))

queue = [root]
while queue:
    n = len(queue)
    print(" ")
    lvl = "Min"
    for i in range(n):
        node = queue.pop(0)
        if node.level % 2 == 1:
            lvl = "Max"
        c = len(node.children)
        print("( ", node.value, c, end=" )")
        for j in range(c):
            queue.append(node.children[j])
        print(" ", lvl, end=(" "))
    print(" ")
    print()
print("Ans is ", root.value)


# def minimax_alpha_beta(array, depth, alpha, beta, maximizing_player):
#     # Base case: check if depth limit reached
#     if depth == 0 or not possible_moves(array):
#         return evaluate(array)

#     if maximizing_player:
#         max_eval = -math.inf
#         for move in possible_moves(array):
#             array[move] = 'X'
#             eval = minimax_alpha_beta(array, depth - 1, alpha, beta, False)
#             array[move] = None  # undo the move
#             max_eval = max(max_eval, eval)
#             alpha = max(alpha, eval)
#             if beta <= alpha:
#                 break  # beta cut-off
#         return max_eval
#     else:
#         min_eval = math.inf
#         for move in possible_moves(array):
#             array[move] = 'O'
#             eval = minimax_alpha_beta(array, depth - 1, alpha, beta, True)
#             array[move] = None  # undo the move
#             min_eval = min(min_eval, eval)
#             beta = min(beta, eval)
#             if beta <= alpha:
#                 break  # alpha cut-off
#         return min_eval


# def evaluate(array):
#     # Simple evaluation function: sum of the numbers in the array
#     return sum(x for x in array if isinstance(x, int))


# def possible_moves(array):
#     # Find empty positions on the array
#     return [i for i, x in enumerate(array) if x is None]


# def dfs_solve(array, depth):
#     if depth == 0 or not possible_moves(array):
#         return evaluate(array)

#     best_score = -math.inf
#     for move in possible_moves(array):
#         array[move] = 'X'
#         score = dfs_solve(array, depth - 1)
#         array[move] = None
#         best_score = max(best_score, score)
#     return best_score


# # Example usage
# random.seed(42)  # for reproducibility
# # random array of length 10 with some elements set to None
# initial_array = [random.randint(
#     1, 100) if random.random() < 0.5 else None for _ in range(10)]
# # initial_array = [random.randint(1, 100)]
# best_score = dfs_solve(initial_array, 3)
# print("Initial array: ", initial_array)
# print("Best Score (DFS):", best_score)
