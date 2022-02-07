import networkx as nx

import matplotlib.pyplot as plt
import random

from graph_search.dfs import dfs
from graph_search.bfs import bfs

if __name__ == '__main__':

    # initialize G
    G = nx.random_regular_graph(3, 10)
    H = nx.random_regular_graph(2, 20)
    H.remove_nodes_from(list(range(10)))
    G.add_edges_from(H.edges)

    # find connected vertexes from node 1
    # res = dfs(12, G)
    res = bfs(1, G)
    print(res)

    weights = {edge: random.randint(0, 50) for edge in G.edges}
    nx.set_edge_attributes(G, weights, name="weight")
    nx.draw(nx.minimum_spanning_tree(G, algorithm="prim"), with_labels=True)
    plt.show()
    nx.draw(nx.minimum_spanning_tree(G, algorithm="kruskal"), with_labels=True)
    plt.show()

