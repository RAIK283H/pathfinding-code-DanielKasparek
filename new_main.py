from graph_data import graph_data
import permutation

if __name__ == "__main__":
    graph = graph_data[10]

    permutations = permutation.steinhaus_johnson_trotter(len(graph) - 2)
    print("All permutations of graph nodes excluding start and end nodes:")
    print(permutations)
    all_hamiltonian_cycles = permutation.find_hamiltonian_cycles(graph)
    print("All Hamiltonian cycles:")
    print(all_hamiltonian_cycles)