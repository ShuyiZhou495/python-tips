import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # Initialize a graph
    G = nx.Graph() # no direction
    D = nx.DiGraph() # has direction

    # Create some types of graph

    H = nx.path_graph(5)
    # looks like
    # 0 - 1 - 2 - 3 - 4


    # Add nodes

    G.add_node(10)
    G.add_nodes_from([20, 30])
    G.add_nodes_from(H)


    # Add edges

    G.add_edge(1, 2)
    # you can add edge with a not-existing node like 8 or 100
    G.add_edges_from([(20, 30), (2, 8), (10, 100)])
    G.add_edges_from(H.edges)
    # weighted edge

    G.add_weighted_edges_from([(8, 2, 0.125), (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])
    # weight is saved in G[8][2]['weight']

    G.add_nodes_from([
        (12, {"color": "red"}),
        (13, {"color": "green"}),
    ])

    # Draw
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

    # Show the elements
    print('----------------')
    print("all nodes:", G.nodes)
        # iterate
    for v in G.nodes:
        pass
    for e in G.edges:
        pass

    # get adjacent nodes of a node
    print('----------------')
    for c in G[2]:
        print(c, end=", ")

    print("adjacent of node 2:", list(G.adj[2]))

    # set property of edge 2-8: (dictionary)
    print('----------------')
    G[2][8]['color'] = 'red'
    G[2][8]['visited'] = True
    print("edge 2 and 8 property:", G[8][2]) # same as G[2][8]

    # get degree of node
    print('----------------')
    print("degree of node 2:", G.degree[2])

    print("degree of node 2 and 3:", G.degree([2, 3]))

    # get edges containing certain nodes
    print('----------------')
    print("edges contains node 2 or 1:", G.edges([2, 1]))

    # set attributes of all the nodes
    nx.set_node_attributes(G, False, "visited")

    # get attributes of all the edges
    print('----------------')
    for (u, v, weight) in G.edges.data('weight'):
        print(u, v, weight)

    # get attributes of all the edges
    for (u, weight) in G.nodes.data('visited'):
        print(u, weight)

    # Remove

    G.remove_node(100)
    G.remove_nodes_from([3, 4])
    G.remove_edge(1, 2)
    G.remove_edges_from([(1, 2), (2, 10)])

    # Draw
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()