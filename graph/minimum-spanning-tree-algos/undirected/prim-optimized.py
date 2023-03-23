"""
Criteria
* For connected and undirected graph

Time Complexity - O ( (V+E) log V )
Space Complexity - O ( V )

Min Heap Implementation: https://ide.geeksforgeeks.org/ziRyEgablT

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
import heapdict
# Heapdict is nothing but Priority Queue
# heapdict - is diff module. Requires pip install

class Solution:
    def prim_mst(self, V, adj):

        # result variables
        mst_edges_child_to_parent = [ i for i in range(V) ]
        mst_weight = 0

        # 1) Create a set mstSet that keeps track of vertices already included in MST.
        visited = [False] * V

        # Todo Time - O( V )
        # 2) Assign a key value to all vertices in the input graph. Initialize all key values as INFINITE.
        vertex_to_min_weight = [sys.maxsize] * V
        # Assign the key value as 0 for the first vertex so that it is picked first.
        # Priority Queue to reduce min search time
        vertex_to_min_weight[0] = 0
        # enumerate 's return type is class enumerate
        vertex_to_min_weight = heapdict.heapdict(enumerate(vertex_to_min_weight))

        # Todo Time - O( V )
        for vertex in range(V-1): #Imp V-1
            # 3 a) Pick a vertex u which is not there in mstSet and has a minimum key value.
            # Pops out as key, priority
            # Todo Time - O( log V )
            min_vertex, min_weight = vertex_to_min_weight.popitem()

            # 3 b) Include u to mstSet.
            visited[min_vertex] = True

            # c) Update key value of all adjacent vertices of u. To update the key values, iterate through all adjacent vertices.
            # For every adjacent vertex v, if the weight of edge u-v is less than the previous key value of v,
            # update the key value as the weight of u-v
            # Todo For V-1 iterations --> TOTAL Time  O( E log V )
            for v, w in adj[min_vertex]:
                if not visited[v] and vertex_to_min_weight[v] > w:
                    # Todo Time - O( log V )
                    # Key - which is 'v' here can hold more meta-data if required for any other scenario
                    vertex_to_min_weight[v] = w
                    # Update result
                    mst_edges_child_to_parent[v] = min_vertex

            # Todo Total Time complexity --> max[ (V log V) + (E log V) ]

            mst_weight = sum(vertex_to_min_weight)
            return mst_weight

