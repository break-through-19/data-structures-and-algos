# https://www.geeksforgeeks.org/dsa/0-1-bfs-shortest-path-binary-graph/
# Related problem: https://www.interviewbit.com/problems/min-cost-path/
"""
Can be used for both directed and undirected graph


TC: O(|V| + |E|)
SC: O(|V| + |E|)
"""

from collections import deque
import sys


def minDist(n, src, adj):
    # Initialize distances to infinity
    # visited array is not used and dist is treated as visited array
    # The first time dist is set with a value other than infinity its considered visited
    # You will not encounter a value lesser than that
    dist = [sys.maxsize] * n
    dist[src] = 0

    # Use deque for 0-1 BFS
    dq = deque()
    dq.append(src)

    while dq:
        u = dq.popleft()

        # Process all adjacent vertices
        for edge in adj[u]:
            v = edge[0]
            weight = edge[1]

            # If we can improve the distance
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

                # If weight is 0, push to front (higher priority)
                # If weight is 1, push to back (lower priority)
                if weight == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)

    return dist


def main():
    n = 9
    src = 0
    edges = [
        (0, 1, 0), (0, 7, 1), (1, 2, 1), (1, 7, 1),
        (2, 3, 0), (2, 5, 0), (2, 8, 1), (3, 4, 1), (3, 5, 1),
        (4, 5, 1), (5, 6, 1), (6, 7, 1), (7, 8, 1)
    ]

    # Create adjacency list representation of the graph
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    res = minDist(n, src, adj)
    for i in range(n):
        print(res[i], end=' ')
    print()


if __name__ == "__main__":
    main()


