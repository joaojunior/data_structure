import unittest

from graph import Graph, Edge


def create_edge(source, dest, value):
    return Edge(source, dest, value)


def verify_graph(graph, nodes, edges):
    if graph.number_of_nodes != len(nodes):
        return False
    if graph.number_of_edges != len(edges):
        return False
    if graph.nodes != nodes:
        return False
    if graph.edges != edges:
        return False
    return True


class TestEmptyGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_size(self):
        self.assertEqual(0, self.graph.number_of_edges)
        self.assertEqual(0, self.graph.number_of_nodes)

    def test_insert_edge(self):
        edge = create_edge(0, 1, 10)
        self.graph.insert(edge)
        self.assertEqual(1, self.graph.number_of_edges)
        self.assertEqual(2, self.graph.number_of_nodes)

    def test_remove_edge(self):
        result = self.graph.remove(source=0, dest=1)
        self.assertEqual(None, result)

    def test_remove_node(self):
        pass


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_insert_two_edges(self):
        edge1 = create_edge(0, 1, 10)
        edge2 = create_edge(0, 2, 20)
        self.graph.insert(edge1)
        self.graph.insert(edge2)
        expected_nodes = set([0, 1, 2])
        expected_edges = {(0, 1): edge1,
                          (0, 2): edge2}
        result = verify_graph(self.graph, expected_nodes, expected_edges)
        self.assertTrue(result)

    def test_insert_three_edges(self):
        edge1 = create_edge(0, 1, 10)
        edge2 = create_edge(0, 2, 20)
        edge3 = create_edge(1, 3, 20)
        self.graph.insert(edge1)
        self.graph.insert(edge2)
        self.graph.insert(edge3)
        expected_nodes = set([0, 1, 2, 3])
        expected_edges = {(0, 1): edge1,
                          (0, 2): edge2,
                          (1, 3): edge3}
        result = verify_graph(self.graph, expected_nodes, expected_edges)
        self.assertTrue(result)

    def test_remove_one_from_two_edges(self):
        edge1 = create_edge(0, 1, 10)
        edge2 = create_edge(0, 2, 20)
        self.graph.insert(edge1)
        self.graph.insert(edge2)
        expected_nodes = set([0, 1, 2])
        expected_edges = {(0, 1): edge1}

        self.graph.remove(edge2.source, edge2.dest)
        result = verify_graph(self.graph, expected_nodes, expected_edges)
        self.assertTrue(result)

    def test_remove_all_edges(self):
        edge1 = create_edge(0, 1, 10)
        edge2 = create_edge(0, 2, 20)
        self.graph.insert(edge1)
        self.graph.insert(edge2)
        expected_nodes = set([0, 1, 2])
        expected_edges = {}

        self.graph.remove(edge1.source, edge1.dest)
        self.graph.remove(edge2.source, edge2.dest)
        result = verify_graph(self.graph, expected_nodes, expected_edges)
        self.assertTrue(result)

    def test_verify_edge_exist_when_edge_exist(self):
        edge1 = create_edge(0, 1, 10)
        self.graph.insert(edge1)

        self.assertTrue(self.graph.edge_exist(edge1.source, edge1.dest))

    def test_verify_edge_exist_when_edge_not_exist(self):
        edge1 = create_edge(0, 1, 10)

        self.assertFalse(self.graph.edge_exist(edge1.source, edge1.dest))

    def test_remove_one_node(self):
        pass

    def test_remove_all_nodes(self):
        pass


if __name__ == '__main__':
    unittest.main()
