import math
import unittest
import graph_data
import global_game_data
from pathing import get_dfs_path, get_bfs_path
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

if __name__ == '__main__':
    unittest.main()
