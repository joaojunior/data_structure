class Edge():
    def __init__(self, source, dest, value):
        self.source = source
        self.dest = dest
        self.value = value


class Graph():
    def __init__(self):
        self.edges = {}
        self.nodes = set()

    @property
    def number_of_edges(self):
        return len(self.edges)

    @property
    def number_of_nodes(self):
        return len(self.nodes)

    def insert(self, edge):
        self.nodes.add(edge.source)
        self.nodes.add(edge.dest)
        self.edges[(edge.source, edge.dest)] = edge

    def remove(self, source, dest):
        edge = None
        if (source, dest) in self.edges:
            pass
        return edge
