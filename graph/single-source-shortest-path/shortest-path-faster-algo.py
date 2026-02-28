
"""
# https://www.geeksforgeeks.org/shortest-path-faster-algorithm/


"""

from collections import deque
import sys

"""
adj[u] = [[v1, w1], [v2, w2].. [vn, wn]]
"""
def shortest_path_faster_algorithm(adj):

    V = len(adj)

    #Todo - SC: O(|V|)
    queue = deque([])
    inQueue = [False] * V
    min_dist = [sys.maxsize] * V

    queue.append(0)
    inQueue[0] = True
    min_dist[0] = 0

    #Todo: Theoritically O(VE) is possible, but in most cases average time complexity is O(E)
    while queue:
        node = queue.popleft()
        inQueue[node] = False

        for v, w in adj[node]:
            if min_dist[v] > min_dist[node] + w:
                min_dist[v] = min_dist[node] + w

                if not inQueue[v]:
                    queue.append(v)
                    inQueue[v] = True

    return min_dist

