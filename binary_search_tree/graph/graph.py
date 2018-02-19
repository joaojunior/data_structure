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
            edge = self.edges.pop((source, dest))
        return edge

    def edge_exist(self, source, dest):
        return (source, dest) in self.edges

    def remove_node(self, node):
        edges_to_remove = []
        if node in self.nodes:
            self.nodes.remove(node)
            for edge in self.edges:
                if edge[0] == node or edge[1] == node:
                    edges_to_remove.append(edge)
        for edge in edges_to_remove:
            self.remove(edge[0], edge[1])
