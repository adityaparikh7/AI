import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  # Cost from start to current node
        self.h = h  # Heuristic estimate from current node to goal

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, node1, node2, cost):
        self.edges.setdefault(node1, []).append((node2, cost))
        self.edges.setdefault(node2, []).append((node1, cost))

    def __str__(self):
        result = ""
        for node, neighbors in self.edges.items():
            result += f"{node} -> {neighbors}\n"
        return result

def astar_search(graph, start, goal, heuristic):
    priority_queue = [Node(start, None, 0, heuristic(start, goal))]
    visited = set()
    cost_so_far = {start: 0}

    while priority_queue:
        current_node = heapq.heappop(priority_queue)

        # print(f"Visiting {current_node.state} with f={current_node.g + current_node.h}")

        if current_node.state == goal:
            # Reconstruct the path from the goal to the start
            result_path = [current_node.state]
            while current_node.parent is not None:
                current_node = current_node.parent
                result_path.append(current_node.state)
            result_path.reverse()
            return result_path, cost_so_far[goal]

        if current_node.state not in visited:
            visited.add(current_node.state)

            for neighbor, cost in graph.edges[current_node.state]:
                if neighbor not in visited:
                    new_cost = cost_so_far[current_node.state] + cost
                    heapq.heappush(
                        priority_queue, Node(neighbor, current_node, new_cost, heuristic(neighbor, goal)))
                    cost_so_far[neighbor] = new_cost

    return None, None

# Function to take user input for start and goal nodes
def start_and_goal():
    start_node = input("Enter the start node: ").strip().upper()
    goal_node = input("Enter the goal node: ").strip().upper()
    return start_node, goal_node

def simple_heuristic(node, goal):
    # Modified heuristic to return 0 for simplicity, adjust as needed
    # Heuristic function for this example (assuming straight-line distance)
    return 0

if __name__ == "__main__":
    # Define a sample graph
    sample_graph = Graph()
    sample_graph.add_edge("A", "B", 1)
    sample_graph.add_edge("A", "C", 3)
    sample_graph.add_edge("C", "A", 3)
    sample_graph.add_edge("B", "D", 5)
    sample_graph.add_edge("D", "B", 3)
    sample_graph.add_edge("E", "C", 2)
    sample_graph.add_edge("C", "E", 2)
    print("Input Graph:")
    print(sample_graph)
    start_node, goal_node = start_and_goal()

    path, total_cost = astar_search(sample_graph, start_node, goal_node, simple_heuristic)
    if path:
        print("Shortest path:", path)
        print("Total cost:", total_cost)
    else:
        print("No path found.")
