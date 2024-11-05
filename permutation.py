def steinhaus_johnson_trotter(n):
    """
    Generate all permutations of integers 1 to n using the Steinhaus-Johnson-Trotter algorithm.

    Parameters:
    n (int): The number of elements to permute.

    Returns:
    list: A list of all permutations.
    """
    # Start with integers from 1 to n (for nodes 1 to n-1)
    sequence = [(i + 1, -1) for i in range(n)]
    
    def get_mobile_integer(seq):
        mobile_integer = None
        mobile_index = None
        for i, (value, direction) in enumerate(seq):
            neighbor_index = i + direction
            if 0 <= neighbor_index < len(seq) and value > seq[neighbor_index][0]:
                if mobile_integer is None or value > mobile_integer:
                    mobile_integer, mobile_index = value, i
        return mobile_integer, mobile_index

    def swap_and_update_directions(seq, mobile_index):
        value, direction = seq[mobile_index]
        neighbor_index = mobile_index + direction
        seq[mobile_index], seq[neighbor_index] = seq[neighbor_index], seq[mobile_index]

        for i, (val, dir) in enumerate(seq):
            if val > value:
                seq[i] = (val, -dir)

    permutations = []
    while True:
        permutations.append([value for value, _ in sequence])
        mobile_integer, mobile_index = get_mobile_integer(sequence)
        if mobile_integer is None:
            break
        swap_and_update_directions(sequence, mobile_index)

    return permutations

def is_hamiltonian_cycle(graph, path):
    """
    Check if the path is a valid Hamiltonian cycle in the graph.

    Parameters:
    graph (list): The graph represented as a list of nodes and their adjacency lists.
    path (list): A list representing a potential Hamiltonian cycle.

    Returns:
    bool: True if the path is a valid Hamiltonian cycle, False otherwise.
    """
    for i in range(len(path) - 1):
        if path[i + 1] not in graph[path[i]][1]:
            return False
    return True

def find_hamiltonian_cycles(graph):
    """
    Finds all Hamiltonian cycles in the given graph.

    Parameters:
    graph (list): The graph structure as a list of nodes, each node having coordinates and an adjacency list.

    Returns:
    list: A list of valid Hamiltonian cycles (each cycle as a list of nodes), or -1 if none are found.
    """
    n = len(graph)
    valid_cycles = []

    # Generate all permutations of nodes 1 to n-2
    permutations = steinhaus_johnson_trotter(n - 2)

    for path in permutations:
        # Complete the path with start node
        complete_path = path + [path[0]]
        if is_hamiltonian_cycle(graph, complete_path):
            valid_cycles.append(path)

    return valid_cycles if valid_cycles else -1