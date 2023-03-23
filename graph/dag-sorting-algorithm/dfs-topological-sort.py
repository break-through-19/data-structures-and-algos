"""
Time complexity: O( |E| + |V| )
Space complexity: O( |V| ) -> For visited array
"""

class Solution:
    def topoSort(self, V, adj):
        # Code here

        visitorTrack = [False] * V
        reverseTopoSort = []

        def buildRevTopoSort(v, visitorTrack, reverseTopoSort):
            if visitorTrack[v] == True:
                return

            # Marked as visited at the beginning
            visitorTrack[v] = True

            for vertex in adj[v]:
                buildRevTopoSort(vertex, visitorTrack, reverseTopoSort)

            """
            Topological Sorting or Kahn's algorithm is an algorithm that orders a directed acylic graph in a way such that 
            each node appears before all the nodes it points to.
                y1              
              /
            x -- y2
              \
                y3
            So, in the below step y1, y2, y3 will be collected first followed by x
            [y1, y2, y3, x]
            Reverse of this gives topological order
            """
            # But collected as Rev Topo Sort at the end
            reverseTopoSort.append(v)

        for vertex in range(V):
            buildRevTopoSort(vertex, visitorTrack, reverseTopoSort)

        return reverseTopoSort[::-1]

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