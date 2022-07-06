"""
* Used for both directed and undirected graph
* Slightly modified version of Prim spanning tree (though that is applicable only for undirected)

Time Complexity: O ( (V+E) log V )
"""
import heapdict
import sys


class Solution:

    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    def dijkstra(self, V, adj, S):
        # code here

        # Result array
        vertexToMinDistance = [sys.maxsize] * V

        visited = [False] * V

        vertexToDistancePriorityQ = heapdict.heapdict()
        for v in range(V):
            vertexToDistancePriorityQ[v] = sys.maxsize

        vertexToDistancePriorityQ[S] = 0

        # Todo Time complexity O( V )
        for vertex in range(V-1):
            # Todo Time complexity O( log V )
            min_vertex, min_dist = vertexToDistancePriorityQ.popitem()

            # Mark visited and add to the result
            vertexToMinDistance[min_vertex] = min_dist
            visited[min_vertex] = True

            # Todo Total time complexity O( E log V )
            for dest, wgt in adj[min_vertex]:
                # Todo : Only difference between Minimum Spanning and Dijkstra
                # Todo : (min_dist + wgt)
                if not visited[dest] and (min_dist + wgt) < vertexToMinDistance[dest]:
                    vertexToMinDistance[dest] = min_dist + wgt

        # Todo Total Time complexity --> max[ (V log V) + (E log V) ]

        return vertexToMinDistance


# {
#  Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

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