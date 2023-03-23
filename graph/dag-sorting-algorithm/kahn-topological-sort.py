"""
Time complexity: O( |E| + |V| )
Space complexity: O( |V| ) -> For visited array

A DAG G has at least one vertex with in-degree 0 and one vertex with out-degree 0.

Proof: There’s a simple proof to the above fact that a DAG does not contain a cycle which means that all paths
will be of finite length. Now let S be the longest path from u(source) to v(destination). Since S is the longest
path there can be no incoming edge to u and no outgoing edge from v, if this situation had occurred then S would not
have been the longest path
=> indegree(u) = 0 and outdegree(v) = 0
"""

from collections import deque

class Solution:

    # Function to return list containing vertices in Topological order.

    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        # Kahn's Topological Sort Algorithm

        indegree = [0] * V
        topoPath = []
        visitorTrack = [False] * V
        queue = deque()

        # Todo Time Complexity O( E )
        for vertexVs in adj:
            for v in vertexVs:
                indegree[v] += 1

        # Todo Time Complexity O( V )
        for vertex in range(V):
            if indegree[vertex] == 0:
                queue.append(vertex)

        # Todo Time Complexity O( V )
        while queue:
            currentVertex = queue.popleft()
            topoPath.append(currentVertex)
            visitorTrack[currentVertex] = True

            for vertexV in adj[currentVertex]:
                indegree[vertexV] -= 1
                if indegree[vertexV] == 0 and not visitorTrack[vertexV]:
                    queue.append(vertexV)

        return topoPath



#  Driver Code Starts
# Driver Program

import sys

sys.setrecursionlimit(10 ** 6)


def check(graph, N, res):
    if N != len(res):
        return False
    map = [0] * N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        e, N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]

        for i in range(e):
            u, v = map(int, input().split())
            adj[u].append(v)

        ob = Solution()

        res = ob.topoSort(N, adj)

        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends