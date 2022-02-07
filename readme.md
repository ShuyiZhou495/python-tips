# Table of Contents
- [Graph](#graph)
  * [`networkx` library](#-networkx--library)
  * [without `networkx` library](#without--networkx--library)
- [Linked list](#linked-list)
- [Useful functions](#useful-functions)

## Graph
there are files for graphs in all of [useful_functions](./useful_functions), 
[data_structures](./data_structures) and [algorithms](./algorithms)
---
### `networkx` library

A brief introduction of the library is written in [for_networkx.py](./useful_functions/for_networkx.py)

- Normally we use `networkx` library for search.
  - Depth-first-search (dfs): `list(nx.dfs_preorder_nodes(G, starting_node))`
  - Breadth-first-search (bfs): `nx.bfs_tree(G, starting_node).nodes`
  - Minimum-spanning-tree (mst): `nx.minimum_spanning_tree(G)`
- If you need to implement search by yourself using `networkx.Graph` class:
  - Depth-first-search is in [dfs.py](./algorithms/graph_search/dfs.py)
  - Breadth-first-search is in [bfs.py](./algorithms/graph_search/bfs.py)
  - Prim's minimum spanning tree is implemented as `mst_prim(G, source)` in [mst.py](algorithms/graph_search/mst.py)
  - An example of using them is shown in [main_graph.py](./algorithms/main_graph.py). This file also shows:
    - How to set color of the graph:
      - `nx.draw(G, node_color=your_list_of_colors)`
    - How to create random graph: 
      - `nx.random_regular_graph(#degree, #nodes)`
---
### without `networkx` library
      
I wrote a simple implementation of graph class in [graph.py](./data_structures/graph.py).
I don't guarantee there is no bug.

Similar as `networkx`,  directional graph is `DiGraph`,
undirenctional graph is `Graph`.

- dfs is used by `G.dfs(source_node)`
- bfs is used by `G.bfs(source_node)`
- mst is used by `G.mst(source_node)`

---

## Linked list
- list in python is linked list. 
Some functions as reminder are written in [list_usage.py](useful_functions/for_list.py)

- I also wrote a simple `linked_list` class in [linked_list.py](./data_structures/linked_list.py)
- Notice that you need to use 
`__copy__()` deep copy a node or list.

---

## Useful functions
Some other useful functions in [useful_functions](./useful_functions).
- [operator overloading](./useful_functions/operator_overloading.py)
- [useful functions for string](./useful_functions/for_string.py)
  - padding: `f"{a:04}"`
  - precision: `f"{a:.5f}"`
- [how to use heapq](./useful_functions/for_heapq.py)
- Import Some common libraries: [imports.py](./useful_functions/imports.py)