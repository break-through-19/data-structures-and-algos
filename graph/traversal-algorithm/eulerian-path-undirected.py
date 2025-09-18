from collections import deque
# Eulerian Path - A path in which all edges are visited.

class Solution:
    # Reference: https://www.youtube.com/watch?v=8MpoO2zA2l4
    # TC: O(|E|)
    # SC: O(V)
    def findEulerianPath(self, adj_list):
        V = len(adj_list)
        degree = [0] * V

        # Step 1 - Count degree
        E = self.countEdgesWithDegree(adj_list, V, degree)

        # Step 2 - Verify if the Eulerian Path exist
        if not self.hasEulerianPath(V, degree): return []

        # Step 3 - If YES, find the starting node
        startNode = self.findStartNode(V, degree)

        # Step 4 - Perform modified depth first search
        eulerian_path = deque([])
        self.eulerianDfs(startNode, degree, adj_list, eulerian_path)

        return eulerian_path if len(eulerian_path)-1 == E else []

    def countEdgesWithDegree(self, adj_list, V, degree):
        E = 0
        for u in range(V):
            for v in adj_list[u]:
                degree[v] += 1
                degree[u] += 1
                E += 1

        return E

    def hasEulerianPath(self, V, degree):
        oddDegreeVertex = 0

        for v in range(V):
            if degree[v] % 2 == 1:
                oddDegreeVertex += 1
            if oddDegreeVertex >= 2: return False

        return True

    def findStartNode(self, V, degree):
        startNode = 0

        for i in range(V):
            if degree[i] % 2 == 1: return i

            if degree[i] > 0: startNode = i

        return startNode

    def eulerianDfs(self, vertex, degree, adj_list, eulerian_path):

        # Do DFS when there is unvisited edges for a given node
        # This base case is important, because we no longer rely on visited nodes tracking
        # Instead we track visited edges, since the objective is to visit all the edges
        while degree[vertex]:
            degree[vertex] -= 1
            self.eulerianDfs(adj_list[degree[vertex]], degree, adj_list, eulerian_path)

        eulerian_path.appendleft(vertex)










