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
