import heapq

def dijkstra(graph, start):
    d = {node: float('inf') for node in graph}
    d[start] = 0
    pq = [(0, start)]

    while pq:
        c, n = heapq.heappop(pq)

        if c > d[n]:
            continue

        for ne, w in graph[n].items():
            new_d = c + w
            if new_d < d[ne]:
                d[ne] = new_d
                heapq.heappush(pq, (new_d, ne))

    return d


# -------------------------
# INPUT GRAPH
# -------------------------
graph = {}

n = int(input("Enter number of nodes: "))
nodes = input("Enter node names separated by space: ").split()

# Initialize adjacency list
for node in nodes:
    graph[node] = {}

e = int(input("\nEnter number of edges: "))
print("Enter edges in format: node1 node2 weight")

for _ in range(e):
    a, b, w = input().split()
    w = int(w)
    graph[a][b] = w
    graph[b][a] = w  # undirected graph

start = input("\nEnter starting node: ").strip()

# Run Dijkstra
result = dijkstra(graph, start)

# -------------------------
# PRINT RESULT
# -------------------------
print(f"\nShortest distances from {start}:")
for node, dist in result.items():
    print(f"{start} → {node} = {dist}")
