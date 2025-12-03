import heapq

def dijkstra(graph, start):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, node = heapq.heappop(pq)
        
        if current_dist > distance[node]:
            continue
        
        for neighbor, weight in graph[node].items():
            new_dist = current_dist + weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return distance


# -------------------------
# TAKE INPUT FROM USER
# -------------------------

graph = {}

n = int(input("Enter number of nodes: "))

print("Enter node names:")
nodes = []
for _ in range(n):
    node = input().strip()
    nodes.append(node)
    graph[node] = {}

e = int(input("\nEnter number of edges: "))

print("Enter edges in format: node1 node2 weight")
for _ in range(e):
    a, b, w = input().split()
    w = int(w)
    graph[a][b] = w
    graph[b][a] = w   # UNDIRECTED graph

start = input("\nEnter starting node: ").strip()

# Run dijkstra
result = dijkstra(graph, start)

# -------------------------
# PRINT RESULT
# -------------------------
print(f"\nShortest distances from {start}:")
for node, dist in result.items():
    print(f"{start} → {node} = {dist}")
