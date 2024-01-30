# implement 8 puzzles problem and show every iteration

# --------------------------------------------------------------------------------------------------------------------------

class PuzzleNode:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move


def print_puzzle(state):
    for row in state:
        print(" ".join(map(str, row)))
    print()


def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def generate_moves(i, j):
    moves = []
    if i > 0:
        moves.append((-1, 0))  # Move up
    if i < 2:
        moves.append((1, 0))   # Move down
    if j > 0:
        moves.append((0, -1))  # Move left
    if j < 2:
        moves.append((0, 1))   # Move right
    return moves


def apply_move(state, move):
    i, j = get_blank_position(state)
    new_state = [row[:] for row in state]
    ni, nj = i + move[0], j + move[1]
    new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
    return new_state


def solve_8_puzzle_bfs(initial_state):
    initial_node = PuzzleNode(initial_state)
    queue = [initial_node]
    visited = set()

    while queue:
        current_node = queue.pop(0)
        print(f"Move {current_node.move}")
        print_puzzle(current_node.state)

        if current_node.state == goal_state:
            print("Goal state reached!")
            return

        visited.add(tuple(map(tuple, current_node.state)))

        i, j = get_blank_position(current_node.state)
        possible_moves = generate_moves(i, j)

        for move in possible_moves:
            new_state = apply_move(current_node.state, move)
            if tuple(map(tuple, new_state)) not in visited:
                new_node = PuzzleNode(new_state, current_node, move)
                queue.append(new_node)

    print("No solution found.")


# def solve_8_puzzle_dfs(initial_state):
#     initial_node = PuzzleNode(initial_state)
#     stack = [initial_node]
#     visited = set()

#     while stack:
#         current_node = stack.pop()
#         print(f"Move {current_node.move}")
#         print_puzzle(current_node.state)

#         if current_node.state == goal_state:
#             print("Goal state reached!")
#             return

#         visited.add(tuple(map(tuple, current_node.state)))

#         i, j = get_blank_position(current_node.state)
#         possible_moves = generate_moves(i, j)

#         for move in possible_moves:
#             new_state = apply_move(current_node.state, move)
#             if tuple(map(tuple, new_state)) not in visited:
#                 new_node = PuzzleNode(new_state, current_node, move)
#                 stack.append(new_node)

#     print("No solution found.")


# Example initial and goal states
initial_state = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
goal_state = [[1, 2, 3], [4, 6, 0], [7, 5, 8]]

# Solve the puzzle using BFS
print("Solving using BFS:")
solve_8_puzzle_bfs(initial_state)

# # Solve the puzzle using DFS
# print("\nSolving using DFS:")
# solve_8_puzzle_dfs(initial_state)
