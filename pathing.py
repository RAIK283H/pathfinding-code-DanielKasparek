import graph_data
import global_game_data
from numpy import random
import graph
import heapq
import math

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    path = []

    # Get the current graph based on the index
    current_graph = graph_data.graph_data[global_game_data.current_graph_index]

    # Get the index of the target node directly from global_game_data
    target_node_index = global_game_data.target_node[global_game_data.current_graph_index]
    assert(0 <= target_node_index < len(current_graph))

    # Start by randomly choosing a node from the adjacency list of the start node (index 0)
    next_node = random.choice(current_graph[0][1])
    path.append(int(next_node))

    # Traverse until the target node is reached
    while next_node != target_node_index:
        next_node = random.choice(current_graph[next_node][1])
        path.append(int(next_node))

    # Once the target node is reached, continue to the exit node
    exit_node_index = len(current_graph) - 1
    while next_node != exit_node_index:
        next_node = random.choice(current_graph[next_node][1])
        path.append(int(next_node))

    assert(target_node_index in path)
    assert(path[-1] == exit_node_index)

    return path


def dfs_recursive(graph, current_node, target_node, visited, parents):
    # Mark current node as visited
    visited.add(current_node)

    if current_node == target_node:
        return True

    # Recurse for each neighbor
    for neighbor in graph[current_node][1]:
        if neighbor not in visited:
            parents[neighbor] = current_node
            if dfs_recursive(graph, neighbor, target_node, visited, parents):
                return True

    # Target node not found
    return False


def get_dfs_path():
    graph_index = global_game_data.current_graph_index
    current_graph = graph_data.graph_data[graph_index]
    start_node = 0
    target_node = global_game_data.target_node[graph_index]
    end_node = len(current_graph) - 1
    target_node_index = global_game_data.target_node[global_game_data.current_graph_index]


    # Initialize visited set and parents dictionary
    visited = set()
    parents = {start_node: None}

    # DFS from start_node to target_node
    if dfs_recursive(current_graph, start_node, target_node, visited, parents):
        # Backtrack to build the path from start_node to target_node
        path = []
        current_node = target_node
        while current_node is not None:
            path.insert(0, current_node)
            current_node = parents[current_node]

    # Reset visited and parents for the second search, target_node to end_node
    visited.clear()
    parents = {target_node: None}

    # DFS from target_node to end_node
    if dfs_recursive(current_graph, target_node, end_node, visited, parents):
        # Backtrack to build the path from target_node to end_node
        current_node = end_node
        reverse_path = []
        while current_node is not None and current_node != target_node:
            reverse_path.insert(0, current_node)
            current_node = parents[current_node]

        # Combine the two paths
        path.extend(reverse_path)

    assert(target_node_index in path)
    assert(path[-1] == end_node)
    for i in range(len(path) - 1):
        assert path[i + 1] in current_graph[path[i]][1], f"Vertices {path[i]} and {path[i + 1]} are not connected."

    return path


def get_bfs_path():
    graph_index = global_game_data.current_graph_index
    current_graph = graph_data.graph_data[graph_index]
    start_node = 0
    target_node = global_game_data.target_node[graph_index]
    end_node = len(current_graph) - 1
    target_node_index = global_game_data.target_node[global_game_data.current_graph_index]


    # Initialize frontier queue, visited set, and parent mapping for the first BFS phase
    frontier = [start_node]
    visited = set([start_node])
    parents = {start_node: None}

    # BFS to find the path from start_node to target_node
    while frontier:
        current_node = frontier.pop(0)
        if current_node == target_node:
            break

        # Explore neighbors
        for neighbor in current_graph[current_node][1]:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current_node
                frontier.append(neighbor)

    # Backtrack from target_node to start_node
    path = []
    current_node = target_node
    while current_node is not None:
        path.insert(0, current_node)
        current_node = parents[current_node]

    # Reset BFS structures for the second search, from target_node to end_node
    frontier = [target_node]
    visited = set([target_node])
    parents = {target_node: None}

    # BFS to find the path from target_node to end_node
    while frontier:
        current_node = frontier.pop(0)
        if current_node == end_node:
            break

        # Explore neighbors again
        for neighbor in current_graph[current_node][1]:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current_node
                frontier.append(neighbor)

    # Backtrack from end_node to target_node
    reverse_path = []
    current_node = end_node
    while current_node is not None and current_node != target_node:
        reverse_path.append(current_node)
        current_node = parents[current_node]
    
    # Reverse the second half and append to the overall path
    path.extend(reverse_path[::-1])

    assert(target_node_index in path)
    assert(path[-1] == end_node)
    for i in range(len(path) - 1):
        assert path[i + 1] in current_graph[path[i]][1], f"Vertices {path[i]} and {path[i + 1]} are not connected."

    return path


def get_dijkstra_path():
    graph_index = global_game_data.current_graph_index
    current_graph = graph_data.graph_data[graph_index]
    start_node = 0
    target_node = global_game_data.target_node[graph_index]
    exit_node = len(current_graph) - 1

    def dijkstra(graph, start, goal):
        # Priority queue: (distance, node, path_so_far)
        pq = []
        heapq.heappush(pq, (0, start, []))
        visited = set()

        while pq:
            current_distance, current_node, path = heapq.heappop(pq)

            if current_node in visited:
                continue

            # Update visited nodes and path
            visited.add(current_node)
            path = path + [current_node]

            # If goal is reached, return the path
            if current_node == goal:
                return path

            # Explore neighbors
            for neighbor in graph[current_node][1]:
                if neighbor not in visited:
                    distance_to_neighbor = math.sqrt(((graph[current_node][0][0] - graph[neighbor][0][0]) ** 2) 
                                                     + ((graph[current_node][0][1] - graph[neighbor][0][1]) ** 2))
                    heapq.heappush(pq, (current_distance + distance_to_neighbor, neighbor, path))

        return None  # No path found

    # Find shortest path from start to target
    path_to_target = dijkstra(current_graph, start_node, target_node)
    if path_to_target is None:
        raise ValueError("No path found from start to target node.")

    # Find shortest path from target to exit
    path_to_exit = dijkstra(current_graph, target_node, exit_node)
    if path_to_exit is None:
        raise ValueError("No path found from target node to exit.")

    # Combine the two paths, ensuring the target node isn't duplicated
    complete_path = path_to_target + path_to_exit[1:]

    # Postcondition checks
    assert complete_path[0] == start_node, "Path does not start at the start node."
    assert complete_path[-1] == exit_node, "Path does not end at the exit node."
    for i in range(len(complete_path) - 1):
        assert complete_path[i + 1] in current_graph[complete_path[i]][1], \
            f"Vertices {complete_path[i]} and {complete_path[i + 1]} are not connected."

    return complete_path
