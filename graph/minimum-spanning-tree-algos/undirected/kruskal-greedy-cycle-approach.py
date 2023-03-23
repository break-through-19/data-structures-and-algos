"""
Criteria
* For connected and undirected graph

Time complexity - O ( E log E ) OR O ( E log V )
Why OR and not sum - bcoz E can at most be V^2. Hence, log E --> 2 * log V

Space complexity - O ( V )

Algorithm Steps:
1. Sort all the edges in increasing order of their weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
3. Repeat step#2 until there are (V-1) edges in the spanning tree.

"""

class Solution:
    def KruskalMST(self, V, adj):

        # Resulting edges
        mst_edges = []

        # Todo Time- O( E log E )
        # Sorted is a built-in func
        # 1. Sort all the edges in increasing order of their weight.
        adj = sorted(adj, key=lambda x: x[2])

        # Todo Space - O ( V )
        # Union-Find DS to identify if cycle is formed
        parent = [i for i in range(V)]
        rank = [0] * V

        edge_count = 0
        e_itr = 0

        # Todo Time - O(E)
        while edge_count < V and e_itr < len(adj):
            # Current min edge
            u, v, w = adj[e_itr]
            e_itr += 1

            # Todo Time- O( log V )
            parent_u = self.find(u, parent)
            parent_v = self.find(v, parent)

            if not self.has_cycle(parent_u, parent_v):
                mst_edges.append([u, v, w])
                edge_count += 1
                # Todo Time - O(log V) --> since its using ranking and path compression
                # Todo Otherwise O(V). Also its in terms of V and not E - coz there can be only V-1 edges
                self.union(u, v, parent_u, parent_v, parent, rank)
        # Todo Time of loop - O ( E log V )


        return mst_edges

    # Assign parent by performing UNION with least rank parent
    def union(self, parent_u, parent_v, parent, rank):

        # Rank is used for optimizing the height of the tree
        # Greater the rank, greater its horizontal scaling
        # A new parent cannot be assigned to parent with greater height, as it will increase the height of all its children
        if rank[parent_u] > rank[parent_v]:
            parent[parent_v] = parent_u
        elif rank[parent_v] > rank[parent_u]:
            parent[parent_u] = parent_v
        else:
            parent[parent_u] = parent_v
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




