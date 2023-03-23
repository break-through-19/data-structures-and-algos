"""
Time complexity: O( |E| + |V| )
Space complexity: O( |V| ) -> For visited and path stack array
"""

# Function to detect cycle in an undirected graph.
def isCycle(self, V, adj):
    # Code here
    visited = [False] * V
    pathStack = [False] * V

    result = False
    for vertex in range(V):
        result = self.checkIfCyclic(vertex, -1, visited, pathStack, adj)
        if result:
            break

    return result


def checkIfCyclic(self, V, fromVertex, visited, pathStack, adj):
    if pathStack[V] == True:
        return True

    if visited[V] == True:
        return False

    pathStack[V] = True
    visited[V] = True
    result = False

    countOfFrom = 0
    for vertex in adj[V]:
        # Imp condition in case of undirected graph
        # If countOfFrom == 2 it means there is a parallel edge
        # You need to visit the from edge again in that case
        # GFG doesnt have any test to verify this, but this is how you handle it

        # Since its undirectional u -> v and v -> u will be present
        # (vertex != fromVertex) - This condition is imp to ensure you don't circle back and mistake it to be a cycle
        if ((vertex != fromVertex) or countOfFrom == 1) and self.checkIfCyclic(vertex, V, visited, pathStack, adj):
            return True
        else:
            countOfFrom += 1
    pathStack[V] = False

    return result


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
            adj[v].append(u)
        obj = Solution()
        ans = obj.isCycle(V, adj)
        if (ans):
            print("1")
        else:
            print("0")

# } Driver Code Ends