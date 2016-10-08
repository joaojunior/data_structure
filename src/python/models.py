class Node(object):
    def __init__(self):
        self.label = ''
        self.weight = 0


class Graph(object):
    def __init__(self):
        self.nodes = {}

    def number_of_nodes(self):
        return len(self.nodes.keys())


class DirectedGraph(Graph):
    pass


class UndirectedGraph(Graph):
    pass
