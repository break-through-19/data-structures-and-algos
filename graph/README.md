# Graph Basics

Graphs - Data Structure: https://www.scaler.com/topics/data-structures/graph-in-data-structure/

Graphs - Algorithms: https://www.scaler.com/topics/graph-algorithms/

# 📚 Graph Concepts

This section provides categorized insights into core graph theory properties, useful for interviews, algorithm design, and competitive programming.

---

## 🧱 A. Structural Properties

- **Complete Graph**: Every pair of distinct vertices is connected by a unique edge.
- **Edge Count in Complete Graph**: A complete graph with `n` vertices has `n(n-1)/2` edges.
- **Tree Edge Count**: A tree with `n` vertices has exactly `n - 1` edges.
- **Handshaking Lemma**: In an undirected graph, the sum of degrees of all vertices equals `2 × (number of edges)`.
- **Odd Degree Vertices**: The number of vertices with odd degree in any undirected graph is even.

---

## 📊 B. Degree Properties

- **Eulerian Circuit (Undirected)**: Exists if and only if the graph is connected and every vertex has an even degree.
- **Eulerian Circuit (Directed)**: Exists if and only if the graph is strongly connected and every vertex has equal in-degree and out-degree.
- **In/Out Degree Equality**: In a directed graph, sum of all in-degrees = sum of all out-degrees = number of edges.

---

## 🔗 C. Connectivity & Components

- **Connected Graph (Undirected)**: A path exists between every pair of vertices.
- **Strongly Connected Graph (Directed)**: Every vertex is reachable from every other vertex.
- **Bridge (Cut-Edge)**: An edge whose removal increases the number of connected components.
- **Cut Vertex (Articulation Point)**: A vertex whose removal increases the number of connected components.

---

## 🔁 D. Cycles & Acyclicity

- **Cycle in Undirected Graph**: A closed path with no repeated edges or vertices (except the start/end).
- **Cyclic Directed Graph**: Has no vertex with in-degree 0.
- **Directed Acyclic Graph (DAG)**: A directed graph with no cycles.
- **DAG Property**: Always has at least one vertex with in-degree 0 and one with out-degree 0.
- **Cycle Detection**: DFS is commonly used (back edge detection in directed graphs).

---

## 🌲 E. Special Graph Types

- **Tree**: A connected, acyclic graph with exactly `n - 1` edges.
- **Forest**: A collection of disjoint trees (i.e., an acyclic, disconnected graph).
- **Bipartite Graph**: Vertices can be split into two disjoint sets with no intra-set edges.
- **Bipartite Condition**: A graph is bipartite if and only if it has no odd-length cycles.

---

## 🧭 F. Traversals & Orderings

- **Topological Sort**: Linear ordering of vertices such that for every directed edge `u → v`, `u` comes before `v`.
- **Topological Sort Condition**: Only possible in DAGs.
- **DFS Tree**: DFS builds a spanning tree from the start vertex in connected graphs.
- **BFS Tree**: Produces the shortest-path tree in an unweighted graph.

---

## 🎨 G. Graph Coloring

- **Chromatic Number**: The minimum number of colors needed to color a graph so no two adjacent vertices share a color.
- **Brooks' Theorem**: `χ(G) ≤ Δ(G)` for all graphs, except complete graphs and odd cycles.
- **Bipartite Coloring**: Bipartite graphs have chromatic number 2.

---

## ⚙️ H. Edge-Based Properties

- **Bridge Detection**: Use DFS with discovery and low time.
- **Cut Edges in Trees**: All edges in a tree are bridges.
- **Maximum Edge Count**: For `n` vertices, the max number of edges is `n(n-1)/2` in a simple undirected graph.
- **Edge Density**: Ratio of actual edges to maximum possible edges, indicating sparsity or density.

---
