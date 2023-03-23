"""
Time complexity: O( |E| + |V| )
Space complexity: O( |V| ) -> For visited array and queue
"""
from collections import deque

class Solution:

    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        # Bool array works for numeric vertices only
        # Using set() can be extensible and handle any kind of vertex representation
        markVisited = [False] * V
        bfs = []

        def buildBfs(vertex, markVisited):
            # Initialize queue with v as that will be the start point
            queue = deque([vertex])
            bfs = []
            while queue:
                currentNode = queue.popleft()
                if not markVisited[currentNode]:
                    markVisited[currentNode] = True
                    bfs.append(currentNode)
                    # Extend Function
                    queue.extend(adj[currentNode])
            return bfs

        # Handle disconnected components of graph
        for v in range(V):
            if not markVisited[v]:
                bfs = bfs + buildBfs(v, markVisited)

        return bfs




# {
#  Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
        ob = Solution()
        ans = ob.bfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()

# } Driver Code Ends