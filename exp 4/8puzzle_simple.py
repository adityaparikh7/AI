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


def solve_8_puzzle(initial_state, goal_state, method, depth_limit=None):
    start_node = PuzzleNode(initial_state)
    visited = set()
    stack = [start_node] if method == 'dfs' else [start_node]
    queue = [start_node] if method == 'bfs' else []

    while stack or queue:
        current_node = stack.pop() if method == 'dfs' else queue.pop(0)
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
                stack.append(
                    new_node) if method == 'dfs' else queue.append(new_node)

    print("No solution found.")


def menu_driven_solver():
    # Example initial and goal states
    initial_state = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
    goal_state = [[1, 2, 3], [4, 6, 0], [7, 5, 8]]

    while True:
        print("\nMenu:")
        print("1. Solve using BFS")
        print("2. Solve using DFS")
        print("3. Solve using Depth-Limited Search")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        print("Move guide")
        print("(-1,0): Up")
        print("(1,0): Down")
        print("(0,-1): Left")
        print("(0,1): Right")

        if choice == '1':
            print("\nSolving using BFS:")
            solve_8_puzzle(initial_state, goal_state, 'bfs')
        elif choice == '2':
            print("\nSolving using DFS:")
            solve_8_puzzle(initial_state, goal_state, 'dfs')
        elif choice == '3':
            depth_limit = int(
                input("Enter the depth limit for Depth-Limited Search: "))
            print(
                f"\nSolving using Depth-Limited Search (Depth Limit: {depth_limit}):")
            solve_8_puzzle(initial_state, goal_state, 'dfs', depth_limit)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# Run the menu-driven solver
menu_driven_solver()
