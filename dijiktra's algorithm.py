import heapq

def dijkstra(graph, start):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    pq = [(0, start)]


    """distance dictionary stores shortest distance from start → each node.

Initially all are infinity.

Starting node = distance 0.

pq is a min-heap that stores (distance, node)"""
    
    while pq:
        current_dist, node = heapq.heappop(pq) 
        
        """Remove the node with smallest distance."""
        
        if current_dist > distance[node]:
            continue
        """ If the popped distance is greater than the recorded shortest distance, skip processing."""

        for neighbor, weight in graph[node].items():
            new_dist = current_dist + weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor)) 
    return distance

    """Calculate new distance

If it’s smaller than stored distance, update

Push updated distance to priority queue"""

graph = {}

n = int(input("Enter number of nodes: "))

print("Enter node names:")
nodes = []
for _ in range(n):
    node = input().strip()
    nodes.append(node)
    graph[node] = {}

    """ Each node becomes a key in the graph dictionary.

Initially, each node has an empty adjacency list."""


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
