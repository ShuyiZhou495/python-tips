import networkx as nx

def mst_prim(G, source):
    res = nx.Graph()
    weight_total = []
    c = {}
    u = list(G.nodes)
    u.remove(source)
    for node in u:
        c[node] = (G[source][node]['weight'] if node in G[source] else float('inf'), source)
    while u:
        w = min(c, key=c.get)
        res.add_edge(w, c[w][1], weight=c[w][0])
        weight_total += [c[w][0]]
        c.pop(w)
        u.remove(w)
        for node in u:
            if node not in G[w]:
                continue
            else:
                weight = G[w][node]['weight']
                if weight < c[node][0]:
                    c[node] = (weight, w)
    return res, weight_total