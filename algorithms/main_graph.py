import networkx as nx

import matplotlib.pyplot as plt
import random

from graph_search.dfs import dfs
from graph_search.bfs import bfs
from graph_search.mst import mst_prim

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

    ############################################
    # example of mst

    G = nx.random_regular_graph(3, 10)
    weights = {edge: random.randint(0, 50) for edge in G.edges}
    nx.set_edge_attributes(G, weights, name="weight")

    ########## mst algorithm by networkx
    nx.draw(nx.minimum_spanning_tree(G, algorithm="prim"), with_labels=True)
    plt.show()
    # nx.draw(nx.minimum_spanning_tree(G, algorithm="kruskal"), with_labels=True)
    # plt.show()

    ########## implemented by me
    Res, weight = mst_prim(G, 1)
    nx.draw(Res, with_labels=True)
    plt.show()
    print(weight)

