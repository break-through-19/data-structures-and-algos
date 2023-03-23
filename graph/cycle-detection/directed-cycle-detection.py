"""
Time complexity: O( |E| + |V| )
Space complexity: O( |V| ) -> For visited and path stack array
"""
class Solution:

    # Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        visited = [False] * V
        pathStack = [False] * V

        # Goes by the logic that, in a traversing DFS path / recursive tree
        # if a vertex occurs twice there is a cycle
        for vertex in range(V):
            if not visited[vertex] and self.checkIfCyclic(vertex, adj, visited, pathStack):
                return True

        return False

    def checkIfCyclic(self, V, adj, visited, pathStack):
        if pathStack[V] == True:
            return True

        # Imp condition to avoid duplicate visits
        if visited[V] == True:
            return False

        visited[V] = True
        result = False
        pathStack[V] = True
        for vertex in adj[V]:
            result = self.checkIfCyclic(vertex, adj, visited, pathStack)
            if result:
                return True
        pathStack[V] = False
        return result


# {
#  Driver Code Starts
# Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V ,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a ,b = map(int ,input().strip().split())
            adj[a].append(b)
        ob = Solution()

        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends