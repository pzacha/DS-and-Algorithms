class Node:
    id = 1

    def __init__(self, data=None):
        self.id = Node.id
        Node.id += 1
        self.data = data
        self.adjacent = []
        self.visited = False

    def __str__(self):
        return str(self.id) + ' adjacent: ' str([a.id for a in self.adjacent])
    
    def add_adjacent(self, n):
        if n not in self.adjacent:
            self.adjacent.append(n)


class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, n):
        if n not in self.nodes:
            self.nodes.append(n)

    def add_edge(self, frm, to):
        if frm not in self.nodes:
            self.add_node(frm)
        if to not in self.nodes:
            self.add_node(to)
        
        frm.add_adjacent(to)

    def dfs(self, n):
        n.visited = True
        for a in n.adjacent:
            if a.visited = False:
                dfs(a)
            

    def is_empty(self):
        if len(self.nodes) == 0:
            raise Exception("Graph is empty")