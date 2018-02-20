class DFS():
    def dfs(self, source, graph):
        self.graph = graph
        self.visited = {}
        self.result = []
        for node in self.graph.nodes:
            self.visited[node] = False
        self._dfs(source)
        return self.result

    def _dfs(self, source):
        self.visited[source] = True
        self.result.append(source)
        for adjacent in self.graph.adjacents(source):
            if self.visited[adjacent] is False:
                self._dfs(adjacent)
