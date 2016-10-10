import unittest

from ..models import DirectedGraph, UndirectedGraph


class BaseTestGraph(object):
    def test_number_of_nodes_in_new_graph(self):
        self.assertEqual(0, self.graph.number_of_nodes())

    def test_number_of_edges_in_new_graph(self):
        self.assertEqual(0, self.graph.number_of_edges())

    def test_add_node(self):
        actual = self.graph.add_node(label='node1', weight=1)
        self.assertEqual(1, self.graph.number_of_nodes())
        self.assertEqual('node1', actual.label)
        self.assertEqual(1, actual.weight)


class TestDirectedGraph(unittest.TestCase, BaseTestGraph):
    def setUp(self):
        self.graph = DirectedGraph()


class TestUndirectedGraph(unittest.TestCase, BaseTestGraph):
    def setUp(self):
        self.graph = UndirectedGraph()

    def test_add_edge(self):
        node1 = self.graph.add_node(label='node1')
        node2 = self.graph.add_node(label='node2')
        edge = self.graph.add_edge(node1, node2, 'edge1', weight=1)
        self.assertEqual('edge1', edge.label)
        self.assertEqual(node1, edge.node_source)
        self.assertEqual(node2, edge.node_destination)

    def test_get_edge_exist(self):
        node1 = self.graph.add_node(label='node1')
        node2 = self.graph.add_node(label='node2')
        edge = self.graph.add_edge(node1, node2, 'edge1', weight=1)
        self.assertEqual(edge,
                         self.graph.get_edge_between_nodes('node1', 'node2'))
        self.assertEqual(edge,
                         self.graph.get_edge_between_nodes('node2', 'node1'))

    def test_get_edge_not_exist(self):
        self.assertEqual(None,
                         self.graph.get_edge_between_nodes('node1', 'node2'))
        self.assertEqual(None,
                         self.graph.get_edge_between_nodes('node2', 'node1'))
