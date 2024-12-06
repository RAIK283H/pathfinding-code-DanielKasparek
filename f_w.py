import math
import random
from graph_data import graph_data
import global_game_data


def adjacency_list_to_matrix(graph_index):
    """
    Converts the adjacency list of a graph into an adjacency matrix.

    Parameters:
        graph_index: Index of the graph in graph_data.

    Returns:
        matrix: Adjacency matrix representing the graph.
    """
    graph = graph_data[graph_index]
    n = len(graph)

    # Initialize the adjacency matrix with infinity
    matrix = [[float('inf')] * n for _ in range(n)]

    # Distance to self is 0
    for i in range(n):
        matrix[i][i] = 0

    # Populate the matrix with distances from adjacency list
    for i, (coord_i, neighbors) in enumerate(graph):
        for neighbor in neighbors:
            coord_j = graph[neighbor][0]
            # Calculate Euclidean distance between nodes
            distance = math.sqrt((coord_i[0] - coord_j[0])**2 + (coord_i[1] - coord_j[1])**2)
            matrix[i][neighbor] = distance
            matrix[neighbor][i] = distance

    return matrix


def floyd_warshall(matrix):
    """
    Computes the shortest paths between all pairs of nodes in a graph using Floyd-Warshall.

    Parameters:
        matrix: Weighted adjacency matrix of the graph.

    Returns:
        distance_matrix: Matrix of shortest path distances.
        predecessor_matrix: Matrix for reconstructing paths.
    """
    n = len(matrix)
    distance_matrix = [row[:] for row in matrix]  # Copy the input matrix
    predecessor_matrix = [[None if i == j or matrix[i][j] == float('inf') else i for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance_matrix[i][k] + distance_matrix[k][j] < distance_matrix[i][j]:
                    distance_matrix[i][j] = distance_matrix[i][k] + distance_matrix[k][j]
                    predecessor_matrix[i][j] = predecessor_matrix[k][j]

    return distance_matrix, predecessor_matrix


def reconstruct_path(predecessor_matrix, start, end):
    """
    Reconstructs the shortest path from start to end using the predecessor matrix.

    Parameters:
        predecessor_matrix: Matrix of predecessors from Floyd-Warshall.
        start: Starting node.
        end: Ending node.

    Returns:
        path: List of nodes representing the shortest path.
    """
    if predecessor_matrix[start][end] is None:
        return None  # No path exists

    path = []
    current = end
    while current != start:
        path.insert(0, current)
        current = predecessor_matrix[start][current]
    path.insert(0, start)

    return path


def main():
    # Change this to change which graph in graph_data.py to find a path in
    graph_index = 2

    # Set Game Data
    for graph in graph_data:
        if len(graph) >= 3:
            global_game_data.target_node.append(random.randint(1, len(graph) - 2))
        else:
            global_game_data.target_node.append(0)

    target_node_index = global_game_data.target_node[graph_index]
    current_graph = graph_data[graph_index]

    adjacency_matrix = adjacency_list_to_matrix(graph_index)

    # Run Floyd-Warshall
    distances, predecessors = floyd_warshall(adjacency_matrix)

    # Define start and end nodes
    start = 0
    end = len(current_graph) - 1

    # Get the shortest path from start to target
    path_to_target = reconstruct_path(predecessors, start, target_node_index)
    if path_to_target is None:
        print("No path from start to target node.")
        return

    # Get the shortest path from target to end
    path_to_end = reconstruct_path(predecessors, target_node_index, end)
    if path_to_end is None:
        print("No path from target node to end node.")
        return

    # Combine the paths (avoiding duplicate target node)
    complete_path = path_to_target + path_to_end[1:]

    # Calculate total distance
    total_distance = distances[start][target_node_index] + distances[target_node_index][end]

    print("Shortest Path (start -> target -> end):", complete_path)
    print("Total Path Distance:", total_distance)


if __name__ == "__main__":
    main()
