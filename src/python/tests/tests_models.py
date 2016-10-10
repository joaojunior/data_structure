import unittest

from ..models import DirectedGraph, UndirectedGraph


class BaseTestGraph(object):
    def test_number_of_nodes_in_new_graph(self):
        self.assertEqual(0, self.graph.number_of_nodes())

    def test_number_of_edges_in_new_graph(self):
        self.assertEqual(0, self.graph.number_of_edges())


class TestDirectedGraph(unittest.TestCase, BaseTestGraph):
    def setUp(self):
        self.graph = DirectedGraph()


class TestUndirectedGraph(unittest.TestCase, BaseTestGraph):
    def setUp(self):
        self.graph = UndirectedGraph()
