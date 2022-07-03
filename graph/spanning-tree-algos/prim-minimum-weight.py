"""
Time Complexity - O ( V^2 )

Algorithm
1) Create a set mstSet that keeps track of vertices already included in MST.
2) Assign a key value to all vertices in the input graph. Initialize all key values as INFINITE. Assign the key value
as 0 for the first vertex so that it is picked first.
3) While mstSet doesn’t include all vertices
….a) Pick a vertex u which is not there in mstSet and has a minimum key value.
….b) Include u to mstSet.
….c) Update key value of all adjacent vertices of u. To update the key values, iterate through all adjacent vertices.
For every adjacent vertex v, if the weight of edge u-v is less than the previous key value of v, update the key value
as the weight of u-v

"""
import sys


class Solution:
    def prim_mst(self, V, adj):

        # result variables
        mst_edges_child_to_parent = [ i for i in range(V) ]
        mst_weight = 0

        # 1) Create a set mstSet that keeps track of vertices already included in MST.
        visited = [False] * V

        # 2) Assign a key value to all vertices in the input graph. Initialize all key values as INFINITE.
        # Assign the key value as 0 for the first vertex so that it is picked first.
        vertex_to_min_weight = []
        vertex_to_min_weight[0] = 0

        for vertex in range(V):
            # 3 a) Pick a vertex u which is not there in mstSet and has a minimum key value.
            min_vertex = self.unvisited_min_vertex(vertex_to_min_weight, visited)

            # 3 b) Include u to mstSet.
            visited[min_vertex] = True

            # c) Update key value of all adjacent vertices of u. To update the key values, iterate through all adjacent vertices.
            # For every adjacent vertex v, if the weight of edge u-v is less than the previous key value of v,
            # update the key value as the weight of u-v
            for v, w in adj[min_vertex]:
                if vertex_to_min_weight[v] < w and not visited[v]:
                    vertex_to_min_weight[v] = w
                    # Update result
                    mst_edges_child_to_parent[v] = min_vertex

            mst_weight = sum(vertex_to_min_weight)

    def unvisited_min_vertex(self, vertex_to_min_weight, visited):
        min_weight = sys.maxsize
        min_vertex = 0
        for v in range(len(visited)):
            if not visited[v] and vertex_to_min_weight[v] < min_weight:
                min_weight = vertex_to_min_weight[v]
                min_vertex = v

        return min_vertex
