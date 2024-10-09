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


# def get_random_path():
#     # returns list of nodes for path
#     # first node is start, travel nodes until it reaches target, travel nodes until it reaches exit
#     # need to be able to loop though the different graphs
#     # graph_data[a][b][1] = adjacency list of point b in graph a

#     path = []
#     # get first node
#     #path.append(graph_data.graph_data.index(graph_data.graph_data[global_game_data.current_graph_index][0]))
#     path.append(1)
#     # check list of adjacent nodes and pick one at random
#     # while current node is not target node
#     # NEED TO FIX THIS COMPARISON
#     while path[-1] != graph_data.graph_data[global_game_data.current_graph_index].index(global_game_data.current_graph_index[global_game_data.target_node]):
#         # pick a random adjacent node
#         # nextNode = 
#         # append that node
#         current_node = path[-1]
#         # Get the adjacency list of the current node
#         adjacent_nodes = graph_data.graph_data[global_game_data.current_graph_index][current_node][1]
#         print(adjacent_nodes)
#         # Randomly pick the next node from the adjacency list
#         next_node = random.choice(adjacent_nodes)
#         path.append(next_node)

#     # while current node is not exit node
#     #while path[-1] is not graph_data[global_game_data.current_graph_index][length-1]:

#     exit_node = len(graph_data[global_game_data.current_graph_index]) - 1  # Exit node is the last node
#     while path[-1] != exit_node:
#         current_node = path[-1]
#         # Get the adjacency list of the current node
#         adjacent_nodes = graph_data[global_game_data.current_graph_index][current_node][1]
#         # Randomly pick the next node from the adjacency list
#         next_node = random.choice(adjacent_nodes)
#         path.append(next_node)

#     print([path])
#     return path
#     ####################
#     # path = []
#     # current_graph = global_game_data.current_graph_index

#     # # Get the start node (which is always at index 0)
#     # path.append(0)

#     # # Get the index of the target node within the current graph
#     # target_node_index = graph_data.graph_data[current_graph].index(global_game_data.target_node)

#     # # Traverse nodes until the target node is reached
#     # while path[-1] != target_node_index:  # Compare index of target node
#     #     current_node = path[-1]
#     #     # Get the adjacency list of the current node
#     #     adjacent_nodes = graph_data.graph_data[current_graph][current_node][1]
#     #     print(adjacent_nodes)  # For debugging, you can remove it later
#     #     # Randomly pick the next node from the adjacency list
#     #     next_node = random.choice(adjacent_nodes)
#     #     path.append(next_node)

#     # # Now traverse from the target node to the exit node
#     # exit_node = len(graph_data.graph_data[current_graph]) - 1  # Exit node is the last node
#     # while path[-1] != exit_node:
#     #     current_node = path[-1]
#     #     # Get the adjacency list of the current node
#     #     adjacent_nodes = graph_data.graph_data[current_graph][current_node][1]
#     #     # Randomly pick the next node from the adjacency list
#     #     next_node = random.choice(adjacent_nodes)
#     #     path.append(next_node)

#     # print([path])  # For debugging, you can remove it later
#     # return path

# def get_random_path():
#     """
#     Traverses the graph starting from a node with (start_x, start_y),
#     randomly picking adjacent nodes until it reaches a node with (target_x, target_y),
#     and then continues to the exit node.
#     """
#     path = []
#     #path.clear()
#     current_graph = global_game_data.current_graph_index

#     # Get start node's x and y coordinates
#     start_x, start_y = graph.Graph.start_x, graph.Graph.start_y
#     target_x, target_y = graph.Graph.target_x, graph.Graph.target_y

#     # Step 1: Find the start node by matching the coordinates
#     start_node_index = None
#     for i, node in enumerate(graph_data.graph_data[current_graph]):
#         if node[0] == (start_x, start_y):
#             start_node_index = i
#             break

#     if start_node_index is None:
#         raise ValueError(f"Start node with coordinates ({start_x}, {start_y}) not found in the current graph.")

#     # Add the start node to the path
#     path.append(int(start_node_index))

#     next_x = -1
#     next_y = -1

#     # Step 2: Traverse nodes randomly until the target node is reached
#     while (next_x, next_y) != (target_x, target_y):
#         current_node = path[-1]
#         # Get the adjacency list of the current node
#         adjacent_nodes = graph_data.graph_data[current_graph][current_node][1]
#         # Randomly pick the next node from the adjacency list
#         next_node = random.choice(adjacent_nodes)
#         path.append(int(next_node))

#         # Get the coordinates of the newly chosen node
#         next_node_coords = graph_data.graph_data[current_graph][next_node][0]
#         next_x, next_y = next_node_coords

#         # # Step 3: Check if the current node is the target node
#         # if (next_x, next_y) == (target_x, target_y):
#         #     break  # Exit the loop when we reach the target

#     # Step 4: Continue to the exit node
#     #exit_node_index = graph_data.graph_data[current_graph][len(graph_data.graph_data[current_graph]) - 1]  # Exit node is the last node
#     exit_node_index = len(graph_data.graph_data[current_graph]) - 1
#     while path[-1] != exit_node_index:
#         current_node = path[-1]
#         adjacent_nodes = graph_data.graph_data[current_graph][current_node][1]
#         next_node = random.choice(adjacent_nodes)
#         path.append(int(next_node))
#     print(path)
#     return path

# def get_random_path():
#     path = []

#     # get a random node from graph array[0]'s adjacency list
#     nextNode = random.choice(graph_data.graph_data[global_game_data.current_graph_index][0][1])
#     path.append(nextNode)

#     while nextNode != graph_data.graph_data[global_game_data.current_graph_index].index(global_game_data.target_node[global_game_data.current_graph_index]):
#         print("nextNode: " + nextNode + "\n")
#         print("targetNode: " + graph_data.graph_data[global_game_data.current_graph_index].index(global_game_data.target_node[global_game_data.current_graph_index]) + "\n")
#         nextNode = random.choice(graph_data[global_game_data.current_graph_index][0][1])
#         path.append(nextNode)

#     while nextNode != graph_data.graph_data[global_game_data.current_graph_index][graph_data.graph_data[global_game_data.current_graph_index][len(graph_data.graph_data[global_game_data.current_graph_index]) - 1]]:
#         nextNode = random.choice(graph_data[global_game_data.current_graph_index][0][1])
#         path.append(nextNode)

#     return path

def get_random_path():
    path = []

    # Get the current graph based on the index
    current_graph = graph_data.graph_data[global_game_data.current_graph_index]

    # Get the index of the target node directly from global_game_data
    target_node_index = global_game_data.target_node[global_game_data.current_graph_index]

    # Start by randomly choosing a node from the adjacency list of the start node (index 0)
    next_node = random.choice(current_graph[0][1])  # Adjacency list of node 0 (start node)
    path.append(int(next_node))

    # Traverse until the target node is reached
    while next_node != target_node_index:
        next_node = random.choice(current_graph[next_node][1])  # Choose a random adjacent node
        path.append(int(next_node))

    # Once the target node is reached, continue to the exit node (last node in the graph)
    exit_node_index = len(current_graph) - 1  # Exit node is the last node
    while next_node != exit_node_index:
        next_node = random.choice(current_graph[next_node][1])  # Choose a random adjacent node
        path.append(int(next_node))

    return path


# accessing target node
#global_game_data.target_node[global_game_data.current_graph_index]

def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
