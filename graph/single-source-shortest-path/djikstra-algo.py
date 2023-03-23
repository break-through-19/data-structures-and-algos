"""
* Used for both Positive Edged directed and undirected graph
* Slightly modified version of Prim spanning tree (though that is applicable only for undirected)

Time Complexity: O ( V^2 )
"""

import sys


class Solution:

    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    def dijkstra(self, V, adj, S):
        # code here

        # Almost same as Prim's MST algo
        # Result array
        vertexToMinDistance = [sys.maxsize] * V
        vertexToMinDistance[S] = 0

        visited = [False] * V

        for vertex in range(V - 1):
            min_vertex = self.get_unvisited_min_distance_vertex(vertexToMinDistance, visited, V)
            min_dist = vertexToMinDistance[min_vertex]

            # Mark visited and add to the result
            visited[min_vertex] = True

            for dest, wgt in adj[min_vertex]:
                # Todo: Only difference between Minimum Spanning and Dijkstra
                # Todo: (min_dist + wgt)
                if not visited[dest] and (min_dist + wgt) < vertexToMinDistance[dest]:
                    vertexToMinDistance[dest] = min_dist + wgt

        return vertexToMinDistance

    def get_unvisited_min_distance_vertex(self, vertexToMinDistance, visited, V):

        min_dist = sys.maxsize
        min_vertex = 0

        for v in range(V):
            if not visited[v] and vertexToMinDistance[v] < min_dist:
                min_dist = vertexToMinDistance[v]
                min_vertex = v

        return min_vertex
    # {


#  Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append([v, w])
            adj[v].append([u, w])
        S = int(input())
        ob = Solution()

        res = ob.dijkstra(V, adj, S)
        for i in res:
            print(i, end=" ")
        print()
# } Driver Code Ends
