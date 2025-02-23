from collections import deque


class Solution:
    # Source: https://www.geeksforgeeks.org/bipartite-graph/
    # Time complexity - O(V+E)
    # Space complexity - O(V)
    def isBipartite(self, adj_list: List[List[int]]) -> bool:
        V = len(adj_list)
        # Colour Map - Takes 0 & 1 as valid colours
        vertex_colours = [-1] * V

        # To handle disconnected components
        for v in range(V):
            if vertex_colours[v] == -1 and not self.bfsBipartiteUtil(v, adj_list, vertex_colours):
                return False

        return True

    def bfsBipartiteUtil(self, src, adj_list, vertex_colours):

        queue = deque([src])
        vertex_colours[src] = 1

        while queue:
            u = queue.popleft()

            for v in adj_list[u]:
                # Self-Loop not acceptable for biparitite
                if u == v or vertex_colours[v] == vertex_colours[u]:
                    return False

                if vertex_colours[v] == -1:
                    vertex_colours[v] = not vertex_colours[u]
                    queue.append(v)

        return True


