"""
Time complexity - O ( E log E )
Algorithm Steps:
1. Sort all the edges in non-decreasing order of their weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
3. Repeat step#2 until there are (V-1) edges in the spanning tree.

"""

class Solution:
    def KruskalMST(self, V, adj):

        # Resulting edges
        mst_edges = []

        # Todo Time- O( E log E )
        # 1. Sort all the edges in non-decreasing order of their weight.
        adj = sorted(adj, key=lambda x: x[2])

        # Todo Space - O ( V )
        # Union - Find DS to find if cycle is formed
        parent = [i for i in range(V)]
        rank = [0] * V

        edge_count = 0
        e_itr = 0

        # Todo Time - O(E)
        while edge_count < V:
            # Current min edge
            u, v, w = adj[e_itr]
            e_itr += 1

            # Todo Time- O( log V )
            parent_u = self.find(u, parent)
            parent_v = self.find(v, parent)

            if not self.has_cycle(parent_u, parent_v):
                mst_edges.append([u, v, w])
                edge_count += 1
                self.union(u, v, parent_u, parent_v, parent, rank)
        # Todo Time of loop - O ( E log V )


        return mst_edges

    # Assign parent by performing union with least rank parent
    def union(self, u, v, parent_u, parent_v, parent, rank):

        # Rank is used for optimization
        if rank[parent_u] > rank[parent_v]:
            parent[u] = parent_v
        elif rank[parent_v] > rank[parent_u]:
            parent[v] = parent_u
        else:
            parent[u] = parent_v
            rank[parent_v] += 1



    def has_cycle(self, parent_u, parent_v):
        return parent_u == parent_v

    # Basically FIND root most parent
    def find(self, u, parent):
        if u == parent[u]:
            return u
        else:
            # Path Compression is used
            return self.find(parent[parent[u]], parent)




