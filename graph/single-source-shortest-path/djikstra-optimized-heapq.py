"""
* Used for both Positive Edged directed and undirected graph
* Slightly modified version of Prim spanning tree (though that is applicable only for undirected)

Time Complexity: O ( (V+E) log V )
Space Complexity: O ( V + E )  # heap can have up to E entries due to lazy deletion

Note: Since heapq doesn't support decrease-key, we use "lazy deletion":
- Push duplicate entries when we find a better distance
- Skip already visited vertices when popping (stale entries)
"""
import heapq
import sys


class Solution:

    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    def dijkstra(self, V, adj, S):

        # Result array
        # Time: O(V)
        vertexToMinDistance = [sys.maxsize] * V
        vertexToMinDistance[S] = 0
        visited = [False] * V

        # Priority Queue: (distance, vertex) - heapq sorts by first element
        # Time: O(1)
        heap = [(0, S)]
        itr = 0
        # Time: O(V + E) iterations total (each vertex processed once, but heap may have up to E entries)
        while heap and itr < V-1:
            # Time: O(log V) per pop
            min_dist, min_vertex = heapq.heappop(heap)

            # Lazy deletion: Skip if already processed (this is a stale entry)
            # Time: O(1)
            if visited[min_vertex]:
                continue

            # Mark visited
            # Time: O(1)
            visited[min_vertex] = True
            itr += 1
            
            # Time: O(degree(min_vertex)) iterations, O(log V) per push
            # Total across all vertices: O(E log V)
            for dest, wgt in adj[min_vertex]:
                # Only difference between Minimum Spanning and Dijkstra: (min_dist + wgt)
                new_dist = min_dist + wgt
                if not visited[dest] and new_dist < vertexToMinDistance[dest]:
                    vertexToMinDistance[dest] = new_dist
                    # Push new entry to heap (old entries become stale)
                    # Time: O(log V)
                    heapq.heappush(heap, (new_dist, dest))

        # Total Time Complexity Breakdown:
        # - Initialization: O(V)
        # - Main loop: processes V vertices
        # - Each heappop: O(log V), total pops can be O(V + E) due to duplicates
        # - Each heappush: O(log V), total pushes O(E)
        # - Total: O(V) + O((V+E) log V) = O((V+E) log V)
        #   Since graph is connected: E >= V-1, so this simplifies to O(E log V)

        return vertexToMinDistance


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = 2, 1
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v, w = 0, 1, 9
            adj[u].append([v, w])
            adj[v].append([u, w])
        S = 0
        ob = Solution()

        res = ob.dijkstra(V, adj, S)
        for i in res:
            print(i, end=" ")
        print()
# } Driver Code Ends
