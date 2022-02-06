import networkx as nx
import matplotlib.pyplot as plt

from graph_search.dfs import dfs
from graph_search.bfs import bfs

if __name__ == '__main__':

    # initialize G
    G = nx.random_regular_graph(3, 10)
    H = nx.random_regular_graph(2, 20)
    H.remove_nodes_from(list(range(10)))
    G.add_edges_from(H.edges)

    nx.draw(G, with_labels=True, node_color='yellow')
    plt.show()

    # find connected vertexes from node 1
    res = dfs(1, G)
    # res = bfs(1, G)
    print(res)

    # plot
    # G.nodes.data('color') can be transformed to dictionary
    colors = list(dict(G.nodes.data('color')).values()) # a list of colors
    nx.draw(G, with_labels=True, node_color=colors)
    plt.show()
