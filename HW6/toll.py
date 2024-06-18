"""
CSCI-665 Assignment 6 - Tolls

This is the program used to determine the minimum time to travel to your destination,
such that your path involves at most two toll roads.

author: Mariam Abidi, Dhruv Dave
reference: Aaron Deever.
"""
import heapq


def dijkstra_with_tolls(n, edges, src, dest):
    """
    Dijkstra's algorithm modified to handle toll roads.

    Args:
    - n: Number of nodes in the graph.
    - edges: List of edges in the graph represented as adjacency lists.
    - src: Source node index.
    - dest: Destination node index.

    Returns:
    - Shortest distance from source to destination considering at most 2 toll roads,
      or -1 if destination is unreachable or toll road limit is exceeded.
    """
    # Initialize distance matrix: dist[i][j] represents shortest distance to reach node i with j tolls
    dist = [[float('inf')] * 3 for _ in range(n)]
    dist[src][0] = 0  # Start node with 0 tolls

    # Priority queue to store nodes based on their distances
    pq = [(0, src, 0)]  # (distance, node, toll_count)

    while pq:
        d, u, toll_count = heapq.heappop(pq)

        # Check if destination is reached
        if u == dest:
            return d

        # Relax neighbors of u
        for v, cost, is_toll in edges[u]:
            new_dist = d + cost
            new_tolls = toll_count + is_toll

            # Check if new distance is smaller or equal and toll count is less than 2
            if new_tolls <= 2 and new_dist < dist[v][new_tolls]:
                # Update distance and toll count for node v
                dist[v][new_tolls] = new_dist
                heapq.heappush(pq, (new_dist, v, new_tolls))

    return -1


# Sample input parsing and function call
n = int(input())
m = int(input())
start = int(input())
end = int(input())

edges = [[] for _ in range(n)]
for _ in range(m):
    u, v, cost, is_toll = map(int, input().split())
    edges[u].append((v, cost, is_toll))
    edges[v].append((u, cost, is_toll))

result = dijkstra_with_tolls(n, edges, start, end)
print(result)
