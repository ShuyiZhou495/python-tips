import networkx as nx

def bfs(n, G: nx.Graph):
    # set attributes
    nx.set_node_attributes(G, False, "visited")
    nx.set_node_attributes(G, 'yellow', "color")

    # set all the nodes' distance to be -1
    nx.set_node_attributes(G, -1, f"distance from {n}")

    # enqueue root
    queue = [(n, 0)]
    visited = [{"node": n, "distance": 0}]

    # set root to be visited and distance to be 0
    G.nodes[n]['visited'] = True
    G.nodes[n][f"distance from {n}"] = 0
    G.nodes[n]['color'] = 'red'

    while(len(queue) !=0 ):
        # dequeue the first node
        node, dis = queue.pop(0)

        # enqueue the neighborhoods and set them visited
        for u in G.adj[node]:
            if not G.nodes[u]['visited']:
                G.nodes[u]['visited'] = True
                G.nodes[u]['color'] = 'red'
                G.nodes[u][f"distance from {n}"] = dis + 1
                queue.append((u, dis + 1))
                visited += [{"node": u, "distance": dis + 1, "from": node}]

    # change everything back
    nx.set_node_attributes(G, False, "visited")
    nx.set_node_attributes(G, 'yellow', "color")
    return visited

