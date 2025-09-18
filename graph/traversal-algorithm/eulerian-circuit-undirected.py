from collections import deque
# Eulerian Circuit - A path in which all edges are visited and the path starts and ends at the same node.

class Solution:
    # Reference: https://www.youtube.com/watch?v=8MpoO2zA2l4
    # TC: O(|E|)
    # SC: O(V)
    def findEulerianCircuit(self, adj_list):
        V = len(adj_list)
        degree = [0] * V

        # Step 1 - Count degree
        E = self.countEdgesInOutDegree(adj_list, V, degree)

        # Step 2 - Verify if the Eulerian Circuit exist
        if not self.hasEulerianCircuit(V, degree): return []

        # Step 3 - If YES, find the starting node
        startNode = self.findStartNode(V, degree)

        # Step 4 - Perform modified depth first search
        eulerian_circuit = deque([])
        self.eulerianDfs(startNode, degree, adj_list, eulerian_circuit)

        return eulerian_circuit if len(eulerian_circuit)-1 == E else []

    def countEdgesWithDegree(self, adj_list, V, degree):
        E = 0
        for u in range(V):
            for v in adj_list[u]:
                degree[v] += 1
                degree[u] += 1
                E += 1

        return E

    def hasEulerianCircuit(self, V, degree):
        for v in range(V):
            if degree[v] % 2 == 1: return False
            
        return True

    def findStartNode(self, V, degree):
        startNode = 0

        for i in range(V):
            if degree[i] > 0: return i

        return startNode

    def eulerianDfs(self, vertex, degree, adj_list, eulerian_circuit):

        # Do DFS when there is unvisited edges for a given node
        # This base case is important, because we no longer rely on visited nodes tracking
        # Instead we track visited edges, since the objective is to visit all the edges
        while degree[vertex]:
            degree[vertex] -= 1
            self.eulerianDfs(adj_list[degree[vertex]], degree, adj_list, eulerian_circuit)

        eulerian_circuit.appendleft(vertex)










