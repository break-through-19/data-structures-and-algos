"""

* Works for directed and undirected graphs with positive edges only
* Negative weight graph is not suitable

Time complexity: O(V^3)

ALGORITHM GIST
We initialize the solution matrix same as the input graph matrix as a first step. Then we update the solution matrix by
considering all vertices as an intermediate vertex. The idea is to one by one pick all vertices and updates all shortest paths
which include the picked vertex as an intermediate vertex in the shortest path. When we pick vertex number k as an intermediate vertex,
we already have considered vertices {0, 1, 2, .. k-1} as intermediate vertices. For every pair (i, j) of the source and
destination vertices respectively, there are two possible cases.
1) k is not an intermediate vertex in shortest path from i to j. We keep the value of dist[i][j] as it is.
2) k is an intermediate vertex in shortest path from i to j. We update the value of dist[i][j] as
dist[i][k] + dist[k][j] if dist[i][j] > dist[i][k] + dist[k][j]


Q: So, what’s the catch?
A: The order of the loops.
for i = 0 to n – 1             for i = 0 to n – 1
    for k = 0 to n – 1             for j = 0 to n – 1
        for j = 0 to n – 1             for k = 0 to n – 1
None of the above works, because the iterator k responsible for intermediate nodes must always be in the outermost loop.
"""


# User function template for Python

class Solution:
    def shortest_distance(self, matrix):
        # Code here

        V = len(matrix)

        # Result is calculated in-place without copying to diff matrix
        # Pick every vertex to be an intermediate vertex one by one
        # Time taken -> 4.96
        for k in range(V):
            for src in range(V):
                for dest in range(V):
                    # As INFINITE is defined as -1 in the input matrix
                    if matrix[src][k] != -1 and matrix[k][dest] != -1:
                        if matrix[src][dest] != -1:
                            matrix[src][dest] = min(matrix[src][dest], matrix[src][k] + matrix[k][dest])
                        else:
                            matrix[src][dest] = matrix[src][k] + matrix[k][dest]


# {
#  Driver Code Starts
# Initial template for Python

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        obj = Solution()
        obj.shortest_distance(matrix)
        for _ in range(n):
            for __ in range(n):
                print(matrix[_][__], end=" ")
            print()
# } Driver Code Ends