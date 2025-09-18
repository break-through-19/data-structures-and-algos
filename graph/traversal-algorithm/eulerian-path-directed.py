from collections import deque
# Eulerian Path - A path in which all edges are visited.

class Solution:
    # Reference: https://www.youtube.com/watch?v=8MpoO2zA2l4
    # TC: O(|E|)
    # SC: O(V)
    def findEulerianPath(self, adj_list):
        V = len(adj_list)
        indegree = outdegree = [0] * V

        # Step 1 - Count In and Out degree
        E = self.countEdgesInOutDegree(adj_list, V, indegree, outdegree)

        # Step 2 - Verify if the Eulerian Path exist
        if not self.hasEulerianPath(V, indegree, outdegree): return []

        # Step 3 - If YES, find the starting node
        startNode = self.findStartNode(V, indegree, outdegree)

        # Step 4 - Perform modified depth first search
        eulerian_path = deque([])
        self.eulerianDfs(startNode, outdegree, adj_list, eulerian_path)

        return eulerian_path if len(eulerian_path)-1 == E else []

    def countEdgesInOutDegree(self, adj_list, V, indegree, outdegree):
        E = 0
        for u in range(V):
            for v in adj_list[u]:
                indegree[v] += 1
                outdegree[u] += 1
                E += 1

        return E

    def hasEulerianPath(self, V, indegree, outdegree):
        startNode = 0
        endNode = 0

        for v in range(V):
            if abs(indegree[v] - outdegree[v]) >= 2: return False
            if outdegree[v] - indegree[v] == 1: startNode += 1
            if indegree[v] - outdegree[v] == 1: endNode += 1

        return (startNode == 0 and endNode == 0) or (startNode == 1 and endNode == 1)

    def findStartNode(self, V, indegree, outdegree):
        startNode = 0

        for i in range(V):
            if outdegree[i] - indegree[i] == 1: return i

            if outdegree[i] > 0: startNode = i

        return startNode

    def eulerianDfs(self, vertex, outdegree, adj_list, eulerian_path):

        # Do DFS when there is unvisited edges for a given node
        # This base case is important, because we no longer rely on visited nodes tracking
        # Instead we track visited edges, since the objective is to visit all the edges
        while outdegree[vertex]:
            outdegree[vertex] -= 1
            self.eulerianDfs(adj_list[outdegree[vertex]], outdegree, adj_list, eulerian_path)

        eulerian_path.appendleft(vertex)










