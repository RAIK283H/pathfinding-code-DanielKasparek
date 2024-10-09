import graph_data
import global_game_data
from numpy import random
import graph

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


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
