from collections import deque

class Solution:
    # Reference: https://www.youtube.com/watch?v=8MpoO2zA2l4
    # TC: O(|E|)
    # SC: O(V)
    def findEulerianCircuit(self, adj_list):
        V = len(adj_list)
        indegree = outdegree = [0] * V

        # Step 1 - Count In and Out degree
        E = self.countEdgesInOutDegree(adj_list, V, indegree, outdegree)

        # Step 2 - Verify if the Eulerian Circuit exist
        if not self.hasEulerianCircuit(V, indegree, outdegree): return []

        # Step 3 - If YES, find the starting node
        startNode = self.findStartNode(V, indegree, outdegree)

        # Step 4 - Perform modified depth first search
        eulerian_circuit = deque([])
        self.eulerianDfs(startNode, outdegree, adj_list, eulerian_circuit)

        return eulerian_circuit if len(eulerian_circuit)-1 == E else []

    def countEdgesInOutDegree(self, adj_list, V, indegree, outdegree):
        E = 0
        for u in range(V):
            for v in adj_list[u]:
                indegree[v] += 1
                outdegree[u] += 1
                E += 1

        return E

    def hasEulerianCircuit(self, V, indegree, outdegree):
        for v in range(V):
            if indegree[v] != outdegree[v]: return False

        return True

    def findStartNode(self, V, indegree, outdegree):
        startNode = 0

        for i in range(V):
            if outdegree[i] - indegree[i] == 1: return i

            if outdegree[i] > 0: startNode = i

        return startNode

    def eulerianDfs(self, vertex, outdegree, adj_list, eulerian_circuit):

        # Do DFS when there is unvisited edges for a given node
        # This base case is important, because we no longer rely on visited nodes tracking
        # Instead we track visited edges, since the objective is to visit all the edges
        while outdegree[vertex]:
            outdegree[vertex] -= 1
            self.eulerianDfs(adj_list[outdegree[vertex]], outdegree, adj_list, eulerian_circuit)

        eulerian_circuit.appendleft(vertex)










