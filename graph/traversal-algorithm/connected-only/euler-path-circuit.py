# Heirholzer Algorithm
# Reconstruct Itinerary - Leet Code
# This is not the complete algorithm, few steps are skipped as those conditions are met by the problem statement
# For complete algo, refer to: eulerian-path-directed
import bisect


class Solution:
    # Reference: https://www.youtube.com/watch?v=8MpoO2zA2l4
    # Heirholzer algorithm
    # TC: O(|E|)
    # SC: O(V)
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj_list = defaultdict(list)
        outdegree = defaultdict(int)
        for src, dest in tickets:
            # Remember - This is to return itinerary in lexical order
            # Bisect modeule provides insort function - inserts in sorted position
            bisect.insort(adj_list[src], dest)
            outdegree[src] += 1

        eulerian_path = deque([])
        self.dfs_by_outdegree("JFK", adj_list, outdegree, eulerian_path)
        return eulerian_path

    def dfs_by_outdegree(self, vertex, adj_list, outdegree, eulerian_path):

        while outdegree[vertex]:
            curr_idx = outdegree[vertex]
            outdegree[vertex] -= 1
            self.dfs_by_outdegree(adj_list[vertex][-curr_idx], adj_list, outdegree, eulerian_path)

        eulerian_path.appendleft(vertex)
        return