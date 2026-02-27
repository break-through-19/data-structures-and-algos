"""
Criteria
* For connected and undirected graph

Time Complexity - O ( (V+E) log V )
Space Complexity - O ( V + E )  # heap can have up to E entries due to lazy deletion

Min Heap Implementation using heapq with lazy deletion approach.

Algorithm
1) Create a set mstSet that keeps track of vertices already included in MST.
2) Assign a key value to all vertices in the input graph. Initialize all key values as INFINITE. Assign the key value
as 0 for the first vertex so that it is picked first.
3) While mstSet doesn't include all vertices
….a) Pick a vertex u which is not there in mstSet and has a minimum key value.
….b) Include u to mstSet.
….c) Update key value of all adjacent vertices of u. To update the key values, iterate through all adjacent vertices.
For every adjacent vertex v, if the weight of edge u-v is less than the previous key value of v, update the key value
as the weight of u-v

Note: Since heapq doesn't support decrease-key, we use "lazy deletion":
- Push duplicate entries when we find a better weight
- Skip already visited vertices when popping (stale entries)

"""
import sys
import heapq

class Solution:
    def prim_mst(self, V, adj):

        # Result variables
        # Time: O(V)
        mst_edges_child_to_parent = [i for i in range(V)]
        mst_weight = 0

        # 1) Create a set mstSet that keeps track of vertices already included in MST.
        # Time: O(V)
        visited = [False] * V

        # 2) Assign a key value to all vertices in the input graph. Initialize all key values as INFINITE.
        # Time: O(V)
        min_weight = [sys.maxsize] * V

        # Assign the key value as 0 for the first vertex so that it is picked first.
        min_weight[0] = 0

        # Priority Queue: (weight, vertex) - heapq sorts by first element
        # Time: O(1) - single push
        heap = [(0, 0)]
        itr = 0

        # 3) While heap is not empty
        # Time: O(V + E) iterations total (each vertex processed once, but heap may have up to E entries)
        while heap and itr < V-1:
            # 3 a) Pick a vertex u which is not there in mstSet and has a minimum key value.
            # Time: O(log V) per pop
            w, u = heapq.heappop(heap)

            # Lazy deletion: Skip if already processed (this is a stale entry)
            # Time: O(1)
            if visited[u]:
                continue

            # 3 b) Include u to mstSet.
            # Time: O(1)
            visited[u] = True
            itr += 1

            # 3 c) Update key value of all adjacent vertices of u.
            # For every adjacent vertex v, if the weight of edge u-v is less than the previous key value of v,
            # update the key value as the weight of u-v
            # Time: O(degree(u)) iterations, O(log V) per push
            # Total across all vertices: O(E log V)
            for v, weight in adj[u]:
                if not visited[v] and weight < min_weight[v]:
                    min_weight[v] = weight
                    mst_edges_child_to_parent[v] = u
                    # Push new entry to heap (old entries become stale)
                    # Time: O(log V)
                    heapq.heappush(heap, (weight, v))

        # Total Time Complexity Breakdown:
        # - Initialization: O(V)
        # - Main loop: processes V vertices
        # - Each heappop: O(log V), total pops can be O(V + E) due to duplicates
        # - Each heappush: O(log V), total pushes O(E)
        # - Total: O(V) + O((V+E) log V) => O((V+E) log V)
        #   Since graph is connected: E >= V-1, so this simplifies to O(E log V)
        mst_weight = sum(min_weight)
        
        return mst_weight, mst_edges_child_to_parent


# Example usage
if __name__ == "__main__":
    # Adjacency list: adj[u] = [(v, weight), ...]
    # Graph:
    #     0 --1-- 1
    #     |       |
    #     2       3
    #     |       |
    #     2 --4-- 3
    adj = [
        [(1, 1), (2, 2)],   # 0 -> 1 (w=1), 0 -> 2 (w=2)
        [(0, 1), (3, 3)],   # 1 -> 0 (w=1), 1 -> 3 (w=3)
        [(0, 2), (3, 4)],   # 2 -> 0 (w=2), 2 -> 3 (w=4)
        [(1, 3), (2, 4)]    # 3 -> 1 (w=3), 3 -> 2 (w=4)
    ]
    sol = Solution()
    weight, parent = sol.prim_mst(4, adj)
    print(f"MST Weight: {weight}")  # Expected: 6 (edges: 0-1, 0-2, 1-3)
    print(f"Parent array: {parent}")
