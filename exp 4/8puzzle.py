# implement 8 puzzles problem and show every iteration

# import copy
# import time
# import random

# class Node:
#     def __init__(self, state, parent, action, path_cost):
#         self.state = state
#         self.parent = parent
#         self.action = action
#         self.path_cost = path_cost

#     def __str__(self):
#         return str(self.state)

#     def __repr__(self):
#         return str(self.state)

#     def __eq__(self, other):
#         return self.state == other.state

#     def __hash__(self):
#         return hash(str(self.state))

#     def __lt__(self, other):
#         return self.path_cost < other.path_cost

#     def __gt__(self, other):
#         return self.path_cost > other.path_cost

#     def __le__(self, other):
#         return self.path_cost <= other.path_cost

#     def __ge__(self, other):
#         return self.path_cost >= other.path_cost

#     def __ne__(self, other):
#         return self.path_cost != other.path_cost

#     def __cmp__(self, other):
#         return self.path_cost.__cmp__(other.path_cost)

#     def expand(self):
#         return [self.child_node(action)
#                 for action in self.actions()]

#     def child_node(self, action):
#         next_state = self.result(action)
#         next_node = Node(next_state, self, action, self.path_cost + 1)
#         return next_node

#     def actions(self):
#         """Return the actions that can be executed in this state."""
#         raise NotImplementedError

#     def result(self, action):
#         """Return the state that results from executing this action."""
#         raise NotImplementedError


# class EightPuzzle(Node):
#     def __init__(self, state, parent=None, action=None, path_cost=0):
#         super().__init__(state, parent, action, path_cost)
#         self.goal_state = [[1,2,3],[4,5,6],[7,8,0]]
#         self.goal = Node(self.goal_state, None, None, 0)

#     def actions(self):
#         """Return the actions that can be executed in this state."""
#         possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
#         return possible_actions

#     def result(self, action):
#         """Return the state that results from executing this action."""
#         new_state = copy.deepcopy(self.state)
#         row, col = self.find_blank(new_state)
#         if action == 'UP':
#             new_state[row][col], new_state[row-1][col] = new_state[row-1][col], new_state[row][col]
#         elif action == 'DOWN':
#             new_state[row][col], new_state[row+1][col] = new_state[row+1][col], new_state[row][col]
#         elif action == 'LEFT':
#             new_state[row][col], new_state[row][col-1] = new_state[row][col-1], new_state[row][col]
#         elif action == 'RIGHT':
#             new_state[row][col], new_state[row][col+1] = new_state[row][col+1], new_state[row][col]
#         return new_state

#     def find_blank(self, state):
#         for i in range(3):
#             for j in range(3):
#                 if state[i][j] == 0:
#                     return i, j

#     def manhattan_distance(self):
#         distance = 0
#         for i in range(3):
#             for j in range(3):
#                 if self.state[i][j] != 0:
#                     distance += abs(i - (self.state[i][j]-1)//3) + abs(j - (self.state[i][j]-1)%3)
#         return distance

#     def __str__(self):
#         return str(self.state[0]) + '\n' + str(self.state[1]) + '\n' + str(self.state[2])

#     def __repr__(self):
#         return str(self.state[0]) + '\n' + str(self.state[1]) + '\n' + str(self.state[2])

#     def __eq__(self, other):
#         return self.state == other.state

#     def __hash__(self):
#         return hash(str(self.state))

#     def __lt__(self, other):
#         return self.manhattan_distance() < other.manhattan_distance()

#     def __gt__(self, other):
#         return self.manhattan_distance() > other.manhattan_distance()

#     def __le__(self, other):
#         return self.manhattan_distance() <= other.manhattan_distance()

#     def __ge__(self, other):
#         return self.manhattan_distance() >= other.manhattan_distance()

#     def __ne__(self, other):
#         return self.manhattan_distance() != other.manhattan_distance()

#     def __cmp__(self, other):
#         return (self.manhattan_distance() > other.manhattan_distance()) - (self.manhattan_distance() < other.manhattan_distance())

# def bfs(initial_state):
#     queue = []
#     queue.append(initial_state)
#     visited = set()
#     visited.add(initial_state)
#     while queue:
#         node = queue.pop(0)
#         if node == node.goal:
#             return node
#         for child in node.expand():
#             if child not in visited:
#                 queue.append(child)
#                 visited.add(child)
#     return None


# def dfs(initial_state):
#     stack = []
#     stack.append(initial_state)
#     visited = set()
#     visited.add(initial_state)
#     while stack:
#         node = stack.pop()
#         if node == node.goal:
#             return node
#         for child in node.expand():
#             if child not in visited:
#                 stack.append(child)
#                 visited.add(child)
#     return None


# def ast(initial_state):
#     queue = []
#     queue.append(initial_state)
#     visited = set()
#     visited.add(initial_state)
#     while queue:
#         queue.sort()
#         node = queue.pop(0)
#         if node == node.goal:
#             return node
#         for child in node.expand():
#             if child not in visited:
#                 queue.append(child)
#                 visited.add(child)
#     return None


# def ida(initial_state):
#     threshold = initial_state.manhattan_distance()
#     while True:
#         result = dls(initial_state, threshold)
#         if result == 'FOUND':
#             return result
#         if result == float('inf'):
#             return None
#         threshold = result


# def dls(initial_state, threshold):
#     stack = []
#     stack.append(initial_state)
#     visited = set()
#     visited.add(initial_state)
#     while stack:
#         node = stack.pop()
#         if node == node.goal:
#             return 'FOUND'
#         if node.manhattan_distance() > threshold:
#             return node.manhattan_distance()
#         for child in node.expand():
#             if child not in visited:
#                 stack.append(child)
#                 visited.add(child)
#     return float('inf')


# def main():
#     initial_state = [[1,2,3],[4,5,6],[7,0,8]]
#     #initial_state = [[1,2,3],[4,5,6],[0,7,8]]
#     #initial_state = [[1,2,3],[4,5,6],[7,8,0]]
#     #initial_state = [[1,2,3],[4,5,6],[8,7,0]]
#     #initial_state = [[1,2,3],[4,5,6],[8,0,7]]
#     #initial_state = [[1,2,3],[4,5,6],[0,8,7]]
#     #initial_state = [[1,2,3],[4,5,6],[8,7,0]]
#     #initial_state = [[1,2,3],[4,5,6],[8,0,7]]
#     #initial_state = [[1,2,3],[4,5,6],[0,8,7]]
#     #initial_state = [[1,2,3],[4,5,6],[8,7,0]]
#     #initial_state = [[1,2,3],[4,5,6],[8,0,7]]
#     #initial_state = [[1,2,3],[4,5,6],[0,8,7]]
#     #initial_state = [[1,2,3],[4,5,6],[8,7,0]]
#     #initial_state = [[1,2,3],[4,5,6],[8,0,7]]
#     #initial_state = [[1,2,3],[4,5,6],[0,8,7]]
#     #initial_state = [[1,2,3],[4,5,6],[8,7,0]]
#     #initial_state = [[1,2,3],[4,5,6],[8,0,7]]
#     #initial_state = [[1,2,3],[4,5,6],[0,8,7]]
#     #initial_state = [[1,2,3],[4,5,6],[8,7,0]]
#     #initial_state = [[1,2,3],[4,5,6],[8,0,7]]
#     #initial_state = [[1,2,3],[4,5,6],[0,
#     #initial_state = [[1,2,3],[4,5,6],[8,7,0]]
#     #initial_state = [[1,2,3],[4,5,6],[8,0,7]]
#     print("Initial state:\n", initial_state)
#     initial_state = EightPuzzle(initial_state)

#     print("BFS:")
#     start = time.time()
#     result = bfs(initial_state)
#     end = time.time()
#     print("Time:", end-start)
#     print("Path cost:", result.path_cost)
#     print("Path:")
#     path = []
#     while result.parent:
#         path.append(result)
#         result = result.parent
#     for i in range(len(path)-1,-1,-1):
#         print(path[i])

#     print("DFS:")
#     start = time.time()
#     result = dfs(initial_state)
#     end = time.time()
#     print("Time:", end-start)
#     print("Path cost:", result.path_cost)
#     print("Path:")
#     path = []
#     while result.parent:
#         path.append(result)
#         result = result.parent
#     for i in range(len(path)-1,-1,-1):
#         print(path[i])

#     print("A*:")
#     start = time.time()
#     result = ast(initial_state)
#     end = time.time()
#     print("Time:", end-start)
#     print("Path cost:", result.path_cost)
#     print("Path:")
#     path = []
#     while result.parent:
#         path.append(result)
#         result = result.parent
#     for i in range(len(path)-1,-1,-1):
#         print(path[i])

#     print("IDA*:")
#     start = time.time()
#     result = ida(initial_state)
#     end = time.time()
#     print("Time:", end-start)
#     print("Path cost:", result.path_cost)
#     print("Path:")
#     path = []
#     while result.parent:
#         path.append(result)
#         result = result.parent
#     for i in range(len(path)-1,-1,-1):
#         print(path[i])

# if __name__ == '__main__':
#     main()

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
