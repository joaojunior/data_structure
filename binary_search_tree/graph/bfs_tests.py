import unittest

from bfs import BFS
from graph import Edge, Graph


def create_edge(source, dest, size):
    return Edge(source, dest, size)


class TestBFS(unittest.TestCase):
    def setUp(self):
        self.bfs = BFS()
        self.graph = Graph()
        self.graph.insert_edge(create_edge(0, 1, 10))
        self.graph.insert_edge(create_edge(0, 2, 20))
        self.graph.insert_edge(create_edge(0, 3, 30))
        self.graph.insert_edge(create_edge(2, 3, 60))
        self.graph.insert_edge(create_edge(3, 4, 120))

    def test_bfs(self):
        result = self.bfs.bfs(0, self.graph)
        expected = [0, 1, 2, 3, 4]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
