import heapq

# -----------------------------------
# Dijkstra Class
# -----------------------------------
class Dijkstra:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = {}

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w   # Undirected graph

    def shortest_path(self, start):
        dist = {node: float('inf') for node in self.graph}
        dist[start] = 0
        pq = [(0, start)]

        while pq:
            c, node = heapq.heappop(pq)

            if c > dist[node]:
                continue

            for neigh, weight in self.graph[node].items():
                new_d = c + weight
                if new_d < dist[neigh]:
                    dist[neigh] = new_d
                    heapq.heappush(pq, (new_d, neigh))

        return dist


# -----------------------------------
# USER INPUT
# -----------------------------------

obj = Dijkstra()

n = int(input("Enter number of nodes: "))
nodes = input("Enter node names separated by space: ").split()

for node in nodes:
    obj.add_node(node)

e = int(input("\nEnter number of edges: "))
print("Enter edges in format: node1 node2 weight")

for _ in range(e):
    u, v, w = input().split()
    obj.add_edge(u, v, int(w))

start = input("\nEnter starting node: ")

# Run Dijkstra using OOP
result = obj.shortest_path(start)

# -----------------------------------
# PRINT RESULT
# -----------------------------------
print(f"\nShortest distances from {start}:")
for node, dist in result.items():
    print(f"{start} → {node} = {dist}")