"""
Time complexity: O( |E| + |V| )
Space complexity: O( |V| ) -> For visited array and indegree

Kahn's is most accurate/well-defined than DFS based topo sort
"""

# Function to return list containing vertices in Topological order.
# From GFG
class Solution:
    def topoSort(self, V, adj):
        # Code here
        # Kahn's Topological Sort Algorithm
        # Impressive - Total Time Taken: 0.77/11.45

        indegree = [0] * V
        topoPath = []
        visitorTrack = [False] * V
        queue = []

        for vertexVs in adj:
            for v in vertexVs:
                indegree[v] += 1

        for vertex in range(V):
            if indegree[vertex] == 0:
                queue.append(vertex)

        while queue:
            currentVertex = queue.pop()
            topoPath.append(currentVertex)
            visitorTrack[currentVertex] = True

            for vertexV in adj[currentVertex]:
                indegree[vertexV] -= 1
                if indegree[vertexV] == 0 and not visitorTrack[vertexV]:
                    queue.append(vertexV)

        return topoPath


# {
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