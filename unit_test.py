import math
import unittest
import graph_data
import global_game_data
import permutation
from pathing import get_dfs_path, get_bfs_path, get_dijkstra_path
from f_w import floyd_warshall, reconstruct_path, adjacency_list_to_matrix
from unittest import mock

class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)


    def test_bfs_path(self):
        graph_data.graph_data = [[
            [(100, 100), [1]],
            [(200, 200), [0, 2, 3]],
            [(300, 300), [1, 4]],
            [(400, 400), [1]],
            [(500, 500), [2]]
        ]]

        target_node = 3
        global_game_data.current_graph_index = 0
        global_game_data.target_node = {0: target_node}

        actual_path = get_bfs_path()
        expected = [0, 1, 3, 1, 2, 4]
        self.assertEqual(actual_path, expected)

    def test_bfs_path_failure(self):
        graph_data.graph_data = [[
            [(100, 100), [1]],
            [(200, 200), [0, 2, 3]],
            [(300, 300), [1, 4]],
            [(400, 400), [1]],
            [(500, 500), [2]]
        ]]

        target_node = 3
        global_game_data.current_graph_index = 0
        global_game_data.target_node = {0: target_node}

        actual_path = get_bfs_path()
        expected = [0, 1, 2, 1, 2, 4]
        self.assertNotEqual(actual_path, expected)

    def test_dfs_path(self):
        graph_data.graph_data = [[
            [(100, 100), [1]],
            [(200, 200), [0, 2, 3]],
            [(300, 300), [1, 4]],
            [(400, 400), [1]],
            [(500, 500), [2]]
        ]]

        target_node = 3
        global_game_data.current_graph_index = 0
        global_game_data.target_node = {0: target_node}

        actual_path = get_dfs_path()
        expected = [0, 1, 3, 1, 2, 4]
        self.assertEqual(actual_path, expected)

    def test_dfs_path_failure(self):
        graph_data.graph_data = [[
            [(100, 100), [1]],
            [(200, 200), [0, 2, 3]],
            [(300, 300), [1, 4]],
            [(400, 400), [1]],
            [(500, 500), [2]]
        ]]

        target_node = 3
        global_game_data.current_graph_index = 0
        global_game_data.target_node = {0: target_node}

        actual_path = get_bfs_path()
        expected = [0, 1, 2, 1, 2, 4]
        self.assertNotEqual(actual_path, expected)


    def test_permutations_of_3(self):
        expected_permutations = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 2, 1],
            [3, 1, 2]
        ]
        result = permutation.steinhaus_johnson_trotter(3)
        self.assertEqual(sorted(result), sorted(expected_permutations))

    def test_permutations_of_4(self):
        result = permutation.steinhaus_johnson_trotter(4)
        self.assertEqual(len(result), 24)  # 4! = 24

    def test_find_hamiltonian_cycles(self):
        # Graph with Hamiltonian cycles:
        graph = [
            [(100, 100), [1, 3]],
            [(0, 0), [0, 2, 3]],
            [(100, 100), [1, 3]],
            [(100, 0), [1, 2, 4]],
            [(200, 100), [3]]
        ]

        # Expected Hamiltonian cycles
        expected_cycles = [
            [1, 2, 3], [1, 3, 2], [3, 1, 2], [3, 2, 1], [2, 3, 1], [2, 1, 3]
        ]

        self.assertEqual(permutation.find_hamiltonian_cycles(graph), expected_cycles)

        # Graph with no Hamiltonian cycle
        graph_no_cycle = [
            [(100, 200), [1]],
            [(0, 0), [0, 2]],
            [(100, 100), [1, 3]],
            [(100, 0), [2, 4]],
            [(200, 100), [3]]
        ]

        self.assertEqual(permutation.find_hamiltonian_cycles(graph_no_cycle), -1)

    def test_dijkstra_path_with_shortest_path_having_more_nodes(self):
        graph_data.graph_data = [[
            [(300, 300), [1, 4]],
            [(350, 350), [0, 2]],
            [(400, 350), [1, 3]],
            [(450, 350), [2, 5]],
            [(0, 0), [0, 5]],
            [(500, 350), [3, 4]]
        ]]

        target_node = 3
        global_game_data.current_graph_index = 0
        global_game_data.target_node = {0: target_node}

        actual_path = get_dijkstra_path()
        expected = [0, 1, 2, 3, 5]
        self.assertEqual(actual_path, expected)

    
    def test_dijkstra_path_with_equal_costs(self):
        graph_data.graph_data = [[
            [(100, 100), [1, 2]],
            [(200, 200), [0, 3]],
            [(200, 200), [0, 3]],
            [(300, 300), [1, 2, 4]],
            [(400, 400), [3, 5]],
            [(500, 500), [4]]
        ]]

        target_node = 3
        global_game_data.current_graph_index = 0
        global_game_data.target_node = {0: target_node}

        actual_path = get_dijkstra_path()
        expected = [0, 1, 3, 4, 5]  # There are multiple paths; any valid shortest path works.
        self.assertEqual(actual_path, expected)

    def test_dijkstra_path_avoids_longer_routes(self):
        graph_data.graph_data = [[
            [(0, 0), [1, 2]],
            [(1, 1), [0, 3]],
            [(2, 2), [0, 4]],
            [(3, 3), [1, 5]],
            [(4, 4), [2, 5]],
            [(5, 5), [3, 4, 6]],
            [(6, 6), []]
        ]]

        target_node = 5
        global_game_data.current_graph_index = 0
        global_game_data.target_node = {0: target_node}

        actual_path = get_dijkstra_path()
        expected = [0, 1, 3, 5, 6]  # Shortest path through Node 4 instead of longer detour.
        self.assertEqual(actual_path, expected)

    def setUp(self):
        """
        Set up sample test graphs and expected results for testing.
        """
        # Graph 1: Simple 3-node triangle graph (fully connected)
        self.graph1 = [
            [(0, 0), [1, 2]],
            [(1, 0), [0, 2]],
            [(0, 1), [0, 1]]
        ]
        self.graph1_matrix = [
            [0, 1, math.sqrt(2)],
            [1, 0, 1],
            [math.sqrt(2), 1, 0]
        ]

        # Graph 2: Disconnected graph
        self.graph2 = [
            [(0, 0), [1]],
            [(1, 0), [0]],
            [(0, 1), []]
        ]
        self.graph2_matrix = [
            [0, 1, float('inf')],
            [1, 0, float('inf')],
            [float('inf'), float('inf'), 0]
        ]

    def test_floyd_warshall(self):
        """
        Test Floyd-Warshall algorithm on a sample graph.
        """
        # Test with graph1
        distances, predecessors = floyd_warshall(self.graph1_matrix)
        expected_distances = self.graph1_matrix  # No changes expected for fully connected graph
        for i in range(len(distances)):
            for j in range(len(distances)):
                self.assertAlmostEqual(distances[i][j], expected_distances[i][j], places=5)

        # Test with graph2
        distances, predecessors = floyd_warshall(self.graph2_matrix)
        self.assertEqual(distances[0][2], float('inf'))
        self.assertEqual(predecessors[0][2], None)

    def test_reconstruct_path(self):
        """
        Test path reconstruction using the predecessor matrix.
        """
        # Test with graph1
        _, predecessors = floyd_warshall(self.graph1_matrix)
        path = reconstruct_path(predecessors, 0, 2)
        self.assertEqual(path, [0, 2])

        # Test with graph2
        _, predecessors = floyd_warshall(self.graph2_matrix)
        path = reconstruct_path(predecessors, 0, 2)
        self.assertIsNone(path)  # No path exists
        

if __name__ == '__main__':
    unittest.main()
