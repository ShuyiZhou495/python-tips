from collections import defaultdict

class GraphBase:
    """
    nodes = {1: {'visited': False}, 2: {'visited': False}}
    edges = {
        1:
            {
                2: {'color': 'red'},
                3: {'color': 'green'}
            },
        2:
            {
                1: {'color': 'red'}
            },
        3:
            {
                1: {'color': 'green'}
            }
    }
    """

    def __init__(self):
        self.nodes = defaultdict(lambda : defaultdict(int))
        self.edges = defaultdict(lambda : defaultdict(lambda: defaultdict(lambda: None)))

    def add_nodes(self, nodes: list):
        for node in nodes:
            if not self.has_node(node):
                self.nodes[node] = defaultdict(lambda: None)

    def add_edges(self, edges: list):
        pass

    def has_node(self, u):
        return u in self.nodes

    def print_nodes(self):
        print("nodes:", list(self.nodes.keys()))

    def print_edges(self):
        res = {}
        for u, us in self.edges.items():
            res[u] = list(us.keys())
        print("edges:", res)

    def set_node_attributes(self, value, label):
        for node in self.nodes:
            self.nodes[node][label] = value

    def remove_nodes(self, nodes):
        pass

    def remove_edges(self, edges):
        pass

    def dfs(self, n):
        res = self.dfs_help(n)
        # change everything back
        self.set_node_attributes(0, "visited")
        return res

    def dfs_help(self, n):
        res = [] # result to return

        if self.nodes[n]["visited"] == 1:
            return []

        self.nodes[n]["visited"] = 1
        res += [n] # if it is not visited, append this node to res

        for u in self.edges[n]:
            res += self.dfs_help(u) # visit the neighbors of n, append the result to res

        return res

    def bfs(self, n):
        # set all the nodes' distance to be -1
        self.set_node_attributes(-1, f"distance from {n}")

        # enqueue root
        queue = [(n, 0)]
        visited = [{"node": n, "distance": 0}]

        # set root to be visited and distance to be 0
        self.nodes[n]['visited'] = 1
        self.nodes[n][f"distance from {n}"] = 0

        while(len(queue) !=0 ):
            # dequeue the first node
            node, dis = queue.pop(0)

            # enqueue the neighborhoods and set them visited
            for u in self.edges[node]:
                if not self.nodes[u]['visited']:
                    self.nodes[u]['visited'] = 1
                    self.nodes[u][f"distance from {n}"] = dis + 1
                    queue.append((u, dis + 1))
                    visited += [{"node": u, "distance": dis + 1, "from": node}]

        # change everything back
        self.set_node_attributes(0, "visited")
        return visited

class Graph(GraphBase):

    def add_edges(self, edges: list):
        for u, v in edges:
            self.add_nodes([u, v])
            if v not in self.edges[u]:
                self.edges[u][v] = defaultdict(lambda: None)
                self.edges[v][u] = defaultdict(lambda: None)

    def degree(self, n):
        return len(self.edges[n])

    def degrees(self):
        return {n: self.degree(n) for n in self.nodes}

    def remove_nodes(self, nodes):
        for node in nodes:
            try:
                self.nodes.pop(node)
                for u in self.edges.pop(node):
                    self.edges[u].pop(node)
            except:
                continue

    def remove_edges(self, edges):
        for u, v in edges:
            try:
                self.edges[u].pop(v)
                self.edges[v].pop(u)
            except:
                continue

class DiGraph(GraphBase):
    """
    edges is out edges
    similar to networkx
    we use inEdges
    """
    inEdges = defaultdict(lambda : defaultdict(lambda: defaultdict(lambda: None)))

    def add_edges(self, edges: list):
        for u, v in edges:
            self.add_nodes([u, v])
            if v not in self.edges[u]:
                self.edges[u][v] = defaultdict(lambda: None)
                self.inEdges[v][u] = defaultdict(lambda: None)

    def print_in_edges(self):
        res = {}
        for u, us in self.inEdges.items():
            res[u] = list(us.keys())
        print("in edges:", res)

    def in_degree(self, n):
        return len(self.inEdges[n])

    def in_degrees(self):
        return {n: self.in_degree(n) for n in self.nodes}

    def out_degree(self, n):
        return len(self.edges[n])

    def out_degrees(self):
        return {n: self.out_degree(n) for n in self.nodes}

    def remove_nodes(self, nodes):
        for node in nodes:
            try:
                self.nodes.pop(node)
                try:
                    for u in self.edges.pop(node):
                        self.inEdges[u].pop(node)
                except:
                    pass
                try:
                    for v in self.inEdges.pop(node):
                        self.edges[v].pop(node)
                except:
                    pass
            except:
                continue

    def remove_edges(self, edges):
        for u, v in edges:
            try:
                self.edges[u].pop(v)
                self.inEdges[v].pop(u)
            except:
                continue


if __name__ == '__main__':
    print("undirectional graph")
    g = Graph()
    g.add_nodes([1, 2, 3, 4,12,13])
    g.add_edges([(1, 2), (2, 1),(2, 12), (3, 4), (12, 13), (4, 12), (5, 6), (4, 5)])
    g.print_nodes()
    g.print_edges()
    print("degrees:", g.degrees())
    print("bfs result: ", g.bfs(1))
    print("dfs result: ", g.dfs(1))


    g.remove_nodes([1, 3, 100])
    g.remove_edges([(1, 2), (12, 13), (1, 5), (200, 1)])


    print("---------------------------")

    print("directional graph")
    h = DiGraph()
    h.add_nodes([1, 2, 3, 4,12,13])
    h.add_edges([(1, 2), (2, 1), (2, 3), (12, 13), (4, 12), (5, 6), (4, 5)])
    print("bfs result: ", h.bfs(1))
    print("dfs result: ", h.dfs(1))
    h.print_in_edges()
    print("out degrees:", h.out_degrees())
    print("in degrees:", h.in_degrees())