import networkx as nx

import matplotlib.pyplot as plt
import random

from graph_search.dfs import dfs
from graph_search.bfs import bfs
from graph_search.mst import mst_prim
from graph_search.dijkstra import dijkstra

def creat_random_splitted_graph():
    G = nx.random_regular_graph(3, 10)
    H = nx.random_regular_graph(2, 20)
    H.remove_nodes_from(list(range(10)))
    G.add_edges_from(H.edges)
    return G

def example_of_dfs_bfs():
    # initialize G
    G = creat_random_splitted_graph()

    # find connected vertexes from node 1
    print("dfs:", dfs(1, G))
    print("bfs:", bfs(1, G))

def create_random_graph_with_weight():
    G = nx.random_regular_graph(3, 10)
    weights = {edge: random.randint(0, 50) for edge in G.edges}
    nx.set_edge_attributes(G, weights, name="weight")
    return G

def example_of_mst(by_me: True):

    # initialize
    G = create_random_graph_with_weight()

    if by_me:
        ########## implemented by me
        Res, weight = mst_prim(G, 1)
        print(weight)
        nx.draw(Res, with_labels=True)
    else:
        ########## mst algorithm by networkx
        nx.draw(nx.minimum_spanning_tree(G, algorithm="prim"), with_labels=True)
        # nx.draw(nx.minimum_spanning_tree(G, algorithm="kruskal"), with_labels=True)
    plt.show()

def example_of_dijkstra():
    # initialize
    G = create_random_graph_with_weight()

    nx.draw(G, with_labels=True)
    plt.show()

    dist, prev = dijkstra(1, G, 'weight')
    print("Distances:", dist)
    print("Predecessors:", prev)



if __name__ == '__main__':

    # example_of_dfs_bfs()

############################################

    # example_of_mst(by_me=True)

############################################

    example_of_dijkstra()

