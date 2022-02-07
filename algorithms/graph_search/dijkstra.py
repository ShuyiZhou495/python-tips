import networkx as nx
from heapq import  heapify, heappop, heappush

def dijkstra(n, G: nx.Graph, s=''):

    # Initialization
    dist = {}
    dist[n] = 0

    prev = {}

    Q = []

    for v in G.nodes:
        if v != n:
            dist[v] = float('inf') # Unknown distance from source to
            prev[v] = None # Predecessor of v
        heappush(Q, (dist[v], v, 1)) # (distance, node, active)

    while len(Q) > 0:
        d, u, act = heappop(Q)
        if act == 0: # already deleted
            continue
        for v in G[u]:
            alt = d + G[u][v][s] if s else d + 1
            if alt < dist[v]:
                # delete the old one by marking it to 0
                for i, j in enumerate(Q):
                    if j[0] == dist[v] and j[1] == v and j[2] == 1:
                        Q[i] = (dist[v], v, 0)
                        break
                dist[v] = alt
                prev[v] = u
                # add the new one
                heappush(Q, (alt, v, 1))
    return dist, prev



