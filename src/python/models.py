class Node(object):
    def __init__(self, label='', weight=0):
        self.label = label
        self.weight = weight


class Edge(object):
    def __init__(self, node_source, node_destination, label='', weight=0):
        self.node_source = node_source
        self.node_destination = node_destination
        self.label = label
        self.weight = weight


class Graph(object):
    def __init__(self):
        self.nodes = []
        self.edges = []

    def number_of_nodes(self):
        return len(self.nodes)

    def number_of_edges(self):
        return len(self.edges)

    def add_node(self, label, weight=0):
        node = Node(label, weight)
        self.nodes.append(node)
        return node


class DirectedGraph(Graph):
    pass


class UndirectedGraph(Graph):
    def add_edge(self, node_source, node_destination, label='', weight=0):
        edge = Edge(node_source, node_destination, label, weight)
        self.edges.append(edge)
        return edge
