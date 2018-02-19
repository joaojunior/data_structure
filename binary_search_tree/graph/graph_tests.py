import unittest

from graph import Graph, Edge


def create_edge(source, dest, value):
    return Edge(source, dest, value)


class TestEmptyGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_size(self):
        self.assertEqual(0, self.graph.number_of_edges)
        self.assertEqual(0, self.graph.number_of_nodes)

    def test_edge_node(self):
        edge = create_edge(0, 1, 10)
        self.graph.insert(edge)
        self.assertEqual(1, self.graph.number_of_edges)
        self.assertEqual(2, self.graph.number_of_nodes)

    def test_remove_edge(self):
        result = self.graph.remove(source=0, dest=1)
        self.assertEqual(None, result)


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_insert_two_edges(self):
        pass

    def test_insert_three_edges(self):
        pass

    def test_remove_one_from_two_edges(self):
        pass

    def test_remove_all_edges(self):
        pass

    def test_verify_edge_exist_when_edge_exist(self):
        pass

    def test_verify_edge_exist_when_edge_not_exist(self):
        pass


if __name__ == '__main__':
    unittest.main()
