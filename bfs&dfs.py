from collections import deque

# BFS Function
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    print("BFS Traversal:", end=" ")

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

# DFS Function
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    print(start, end=" ")
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# ------------------------------
# MAIN PROGRAM WITH USER INPUT
# ------------------------------
graph = {}
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("\nEnter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start = input("\nEnter starting node: ")

print("\n--- BFS OUTPUT ---")
bfs(graph, start)

print("\n\n--- DFS OUTPUT ---")
print("DFS Traversal:", end=" ")
dfs(graph, start)
