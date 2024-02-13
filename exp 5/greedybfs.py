import heapq


def greedy_best_first_search(graph, start, goal, heuristic):
    priority_queue = [(heuristic(start), start)]
    visited = set()
    path = {start: None}

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            # Reconstruct the path from the goal to the start
            result_path = [goal]
            while path[result_path[-1]] is not None:
                result_path.append(path[result_path[-1]])
            result_path.reverse()
            return result_path

        if current_node not in visited:
            visited.add(current_node)

            for neighbor, cost in graph[current_node].items():
                if neighbor not in visited:
                    heapq.heappush(
                        priority_queue, (heuristic(neighbor), neighbor))
                    # Update the path
                    path[neighbor] = current_node

    return None


# Example usage:
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 5},
    'C': {'A': 3, 'E': 2},
    'D': {'B': 5},
    'E': {'C': 2}
}

start_node = 'A'
goal_node = 'E'


def heuristic(node):
    return abs(ord(node) - ord(goal_node))


result_path = greedy_best_first_search(graph, start_node, goal_node, heuristic)

if result_path:
    print(f"Path from {start_node} to {goal_node}: {' -> '.join(result_path)}")
else:
    print(f"No path found from {start_node} to {goal_node}")
