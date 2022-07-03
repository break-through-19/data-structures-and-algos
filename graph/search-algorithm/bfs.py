"""
Time complexity: O( |E| + |V| )
Space complexity: O( |V| ) -> For visted array and queue
"""

class Solution:

    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        markVisited = [False] * V
        bfs = []

        def buildBfs(queue, markVisited):
            bfs = []
            while len(queue) != 0:
                currentNode = queue.pop(0)
                if not markVisited[currentNode]:
                    markVisited[currentNode] = True
                    bfs.append(currentNode)
                    queue = queue + (adj[currentNode])

            return bfs

        # Handle disconnected components of graph
        for v in range(V):
            if not markVisited[v]:
                # Initialize queue with v as that will be the start point
                queue = [v]
                bfs = bfs + buildBfs(queue, markVisited)

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