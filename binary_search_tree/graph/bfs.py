class BFS():
    def bfs(self, source, graph):
        visited = {}
        result = []
        for node in graph.nodes:
            visited[node] = False
        nodes = [source]
        while nodes:
            node = nodes.pop(0)
            if visited[node] is False:
                visited[node] = True
                result.append(node)
                for adjacent in graph.adjacents(node):
                    nodes.append(adjacent)
        return result
