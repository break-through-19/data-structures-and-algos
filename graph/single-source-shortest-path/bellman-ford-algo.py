"""
Bellman Ford Algo
* Works for both negative and positive weights unlike Dijkstra
* Works only for DIRECTED graphs
* Time complexity more than Dijkstra O ( VE )
* Suitable for distributed systems
* Will not work for Negative cycles, for the same reason not suitable for UNDIRECTED graphs (as undirected negative edges would be considered a cycle)

Negative Cycle Definition:
Theoretically, if a graph has cycle and sum of its edges is negative, it is called negative cycle.

Has Neg Cycle,
If dist[v] > dist[u] + weight[u][v]

Time complexity: O ( VE )

Below solution is combination of two problems:
1. Bellman Ford algo for single source shortest path
2. Find if a graph has negative cycle
"""

# User function Template for python3
import sys

class Solution:
    def isNegativeWeightCycle(self, n, edges):
        # Code here

        def bellman_ford_algo(source, min_dist):
            # Bellman Ford Algorithm - to find single source based shortest path
            # Works for directed graphs without negative cycles
            min_dist[source] = 0

            # Traverse vertex-1 times Edges
            # At the end of each iteration, shortest path would be calc for vertices with edge length v
            # KEY POINT: This means optimal answer would be found after max_edge_length iterations
            for v in range(n - 1):
                # Extra logic considering the KEY POINT above
                optimal_calc = False
                for u, v, w in edges:
                    if min_dist[v] > min_dist[u] + w:
                        min_dist[v] = min_dist[u] + w
                        # Extra logic considering the KEY POINT above
                        optimal_calc = True
                # Extra logic considering the KEY POINT above
                if not optimal_calc:
                    break

            # Extension of that to find the negative cycle
            for u, v, w in edges:
                # If you encounter a scenario like this even after N-1 iterations - then Negative cycle exists
                if min_dist[v] > min_dist[u] + w:
                    return 1
            return 0

        min_dist = [sys.maxsize] * n

        # To handle DISCONNECTED components also
        for v in range(n):
            if min_dist[v] == sys.maxsize and bellman_ford_algo(v, min_dist):
                return 1

        return 0


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        edges = []
        for _ in range(m):
            edges.append(list(map(int, input().split())))
        obj = Solution()
        ans = obj.isNegativeWeightCycle(n, edges)
        print(ans)

# } Driver Code Ends