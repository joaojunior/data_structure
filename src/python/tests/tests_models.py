import unittest

from ..models import DirectedGraph, UndirectedGraph


class BaseTestGraph(object):
    def test_number_of_nodes_new_graph(self):
        self.assertEqual(0, self.graph.number_of_nodes())


class TestDirectedGraph(unittest.TestCase, BaseTestGraph):
    def setUp(self):
        self.graph = DirectedGraph()


class TestUndirectedGraph(unittest.TestCase, BaseTestGraph):
    def setUp(self):
        self.graph = UndirectedGraph()
