"""
Time complexity: O( |E| + |V| log V ), however log V is close to constant bcoz of optimizations
Space complexity: O( |V| ) -> For visited and path stack array
"""


from typing import List

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        # Code here

        parent = [i for i in range(V)]
        rank = [0] * V

        edge_set = [set() for i in range(V)]

        # Consider only one of undirected egde
        # Dupes lead to self-loop kinda state and incorrect result
        for u in range(V):
            for v in adj[u]:
                if u not in edge_set[v]:
                    edge_set[u].add(v)

        for u in range(V):
            for v in edge_set[u]:
                # Parent_u shld be calculated for every iteration bcoz, parent keeps changing in union process
                parent_u = self.find(u, parent)
                parent_v = self.find(v, parent)
                if parent_u == parent_v:
                    return True
                self.union(parent_u, parent_v, parent, rank)

        return False


    def find(self, node, parent):
        if node == parent[node]:
            return node
        else:
            return self.find(parent[parent[node]], parent)


    def union(self, parent1, parent2, parent, rank):
        if rank[parent1] > rank[parent2]:
            parent[parent2] = parent1
        elif rank[parent2] > rank[parent1]:
            parent[parent1] = parent2
        else:
            parent[parent2] = parent1
            rank[parent1] += 1