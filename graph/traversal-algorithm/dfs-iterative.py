"""
Time complexity: O( |E| + |V| )
Space complexity: O( |V| ) -> For visited array and queue
"""
from collections import deque


class Solution:

    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        visited = set()
        dfsPath = []

        def buildDfs(visited, adj, vertex):
            stack = deque([vertex])
            dfsPathLocal = []
            while stack:
                curr_vertex = stack.pop()

                if curr_vertex not in visited:
                    dfsPathLocal.append(curr_vertex)
                    visited.add(curr_vertex)

                    stack.extend(adj[curr_vertex][::-1])

            return dfsPathLocal

        for v in range(V):
            if v not in visited:
                dfsPath = dfsPath + buildDfs(visited, adj, v)

        return dfsPath

