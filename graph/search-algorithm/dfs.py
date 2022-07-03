"""
Time complexity: O( |E| + |V| )
Space complexity: O( |V| ) -> For visited array
"""

class Solution:
# From GFG
    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        dfsPath = []
        visited = [False] * V

        # Handle disconnected components of graph
        for vertex in range(V):
            self.buildDfs(visited, vertex, adj, dfsPath)

        return dfsPath

    def buildDfs(self, visited, V, adj, dfsPath):
        if visited[V] == True:
            return

        visited[V] = True
        dfsPath.append(V)

        for vertex in adj[V]:
            self.buildDfs(visited, vertex, adj, dfsPath)


# {
#  Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    while T > 0:
        V, E = map(int, input().split())
        adj = [[] for i in range(V + 1)]
        for i in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob = Solution()
        ans = ob.dfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
        T -= 1
# } Driver Code Ends