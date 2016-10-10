class Node(object):
    def __init__(self):
        self.label = ''
        self.weight = 0


class Graph(object):
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def number_of_nodes(self):
        return len(self.nodes.keys())

    def number_of_edges(self):
        return len(self.edges.keys())


class DirectedGraph(Graph):
    pass


class UndirectedGraph(Graph):
    pass
