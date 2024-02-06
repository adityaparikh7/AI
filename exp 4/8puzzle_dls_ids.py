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


def depth_limited_search(node, goal_state, depth_limit):
    if node.state == goal_state:
        return node

    if depth_limit == 0:
        return None

    i, j = get_blank_position(node.state)
    possible_moves = generate_moves(i, j)

    for move in possible_moves:
        new_state = apply_move(node.state, move)
        new_node = PuzzleNode(new_state, node, move)

        result = depth_limited_search(new_node, goal_state, depth_limit - 1)
        if result:
            return result

    return None


def iterative_deepening_search(initial_state, goal_state):
    depth_limit = 0
    while True:
        result = depth_limited_search(PuzzleNode(
            initial_state), goal_state, depth_limit)
        if result:
            print(f"Solution found at depth {depth_limit}:")
            print_solution(result)
            return
        depth_limit += 1


def print_solution(node):
    path = []
    while node:
        path.append(node)
        node = node.parent

    for t in reversed(path):
        print(f"Move {t.move}")
        print_puzzle(t.state)


# Example initial and goal states
initial_state = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
goal_state = [[1, 2, 3], [4, 6, 0], [7, 5, 8]]

# Solve the puzzle using Iterative Deepening Search
print("Solving using Iterative Deepening Search:")
iterative_deepening_search(initial_state, goal_state)

# Solve the puzzle using Depth-Limited Search
depth_limit = 10  # You can adjust the depth limit as needed
print(f"\nSolving using Depth-Limited Search (Depth Limit: {depth_limit}):")
result = depth_limited_search(PuzzleNode(
    initial_state), goal_state, depth_limit)
if result:
    print_solution(result)
else:
    print("No solution found within the depth limit.")
