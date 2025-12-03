from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    # Add a node and its neighbors
    def add_node(self, node, neighbors):
        self.graph[node] = neighbors

    # BFS Traversal
    def bfs(self, start):
        visited = set()
        queue = deque([start])

        print("BFS Traversal:", end=" ")

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                queue.extend(self.graph[node])


# ------------------------------
# MAIN PROGRAM WITH USER INPUT
# ------------------------------

g = Graph()
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("\nEnter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    g.add_node(node, neighbors)

start = input("\nEnter starting node: ")

print("\n--- BFS OUTPUT ---")
g.bfs(start)
