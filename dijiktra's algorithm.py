import heapq
def dijkstra(graph, start):
    d = {node: float('inf') for node in graph}
    d[start] = 0
    pq = [(0, start)]
    while pq:
        c, n = heapq.heappop(pq)
        # Skip if this distance is outdated
        if c > d[n]:
            continue
        for ne, w in graph[n].items():
            n_d = c + w
            if n_d < d[ne]:
                d[ne] = n_d
                heapq.heappush(pq, (n_d, ne))         
    return d

graph = {}
n = int(input("Enter number of nodes: "))
print("Enter node names:")
nodes = [input().strip() for _ in range(n)]
for node in nodes:
    graph[node] = {}
e = int(input("\nEnter number of edges: "))
print("Enter edges in format: node1 node2 weight")
for _ in range(e):
    a, b, w = input().split()
    w = int(w)
    graph[a][b] = w
    graph[b][a] = w  # UNDIRECTED graph

start = input("\nEnter starting node: ").strip()

# Run Dijkstra
result = dijkstra(graph, start)

# -------------------------
# PRINT RESULT
# -------------------------
print(f"\nShortest distances from {start}:")
for node, dist in result.items():
    print(f"{start} → {node} = {dist}")
