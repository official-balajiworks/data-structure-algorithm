import heapq  # For priority queue

def dijkstra(graph, start):
    # Store shortest distances; start node = 0, others = infinity
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    
    # Priority queue holds (distance, node)
    pq = [(0, start)]
    
    while pq:
        current_dist, node = heapq.heappop(pq)
        
        # Skip if we already have a shorter path
        if current_dist > distance[node]:
            continue
        
        # Check all neighbors
        for neighbor, weight in graph[node].items():
            new_dist = current_dist + weight
            
            # Update if a shorter path is found
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return distance
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Run algorithm
start = 'A'
result = dijkstra(graph, start)

# Print results
print(f"Shortest distances from {start}:")
for node, dist in result.items():
    print(f"{start} → {node} = {dist}")
