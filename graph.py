class Graph:
    """ Bidirectional graph """
    def __init__(self, adj_list = None):
        if adj_list == None:
            self.adj_list = {}
        else:
            self.adj_list = adj_list

    def get_vertices(self):
        return list(self.adj_list.keys())
    
    def get_edges(self):
        edges = []
        for key in self.adj_list.keys():
            for val in self.adj_list[key]:
                edge = sorted(str(key) + str(val))
                if edge not in edges:
                    edges.append(edge)
        return edges

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []

    def add_edge(self, vrtx1, vrtx2):
        if (str(vrtx1) + str(vrtx2)) not in self.get_edges():
            self.adj_list[vrtx1] += vrtx2
            self.adj_list[vrtx1] = sorted(self.adj_list[vrtx1])
            self.adj_list[vrtx2] += vrtx1
            self.adj_list[vrtx2] = sorted(self.adj_list[vrtx2])

    def dfs(self, start, visited = []):
        visited.append(start)
        for vrtx in self.adj_list[start]:
            if vrtx not in visited:
                self.dfs(vrtx, visited)
        return visited

    def bfs(self, start):
        visited = []
        queue = []
        queue.insert(0, start)
        visited.append(start)
        while queue:
            next = queue.pop()
            for vrtx in self.adj_list[next]:
                if vrtx not in visited:
                    visited.append(vrtx)
                    queue.insert(0, vrtx)
        return visited



g = Graph({"a" : ["b","c"], "b" : ["a", "d"], "c" : ["a", "d"], "d" : ["e"], "e" : ["d"]})

print("List of edges: ", g.get_edges())
g.add_edge("a", "d")
print("Added edge a-d: ", g.adj_list)
print("Depth-first search: ", g.dfs('a'))
print("Breadth-first search: ", g.bfs('a'))

