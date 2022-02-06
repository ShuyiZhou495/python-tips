import networkx as nx

def dfs(n, G: nx.Graph):
    # set attributes
    nx.set_node_attributes(G, False, "visited")
    nx.set_node_attributes(G, 'yellow', "color")
    res = dfs_help(n, G)
    # change everything back
    nx.set_node_attributes(G, False, "visited")
    nx.set_node_attributes(G, 'yellow', "color")
    return res

def dfs_help(n, G: nx.Graph):
    res = [] # result to return

    if G.nodes[n]["visited"] == True:
        return []

    G.nodes[n]["visited"] = True
    G.nodes[n]["color"] = 'red'
    res += [n] # if it is not visited, append this node to res

    for u in G.adj[n]:
        res += dfs_help(u, G) # visit the neighbors of n, append the result to res

    return res


