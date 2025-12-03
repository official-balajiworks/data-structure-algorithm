from collections import defaultdict, deque

def topological_sort(graph):
    # Step 1: Find in-degree (number of incoming edges) for each node
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] = in_degree.get(v, 0) + 1

    # Step 2: Create a queue for nodes with in-degree 0
    queue = deque([u for u in in_degree if in_degree[u] == 0])

    top_order = []  # to store the topological order

    # Step 3: Process the queue
    while queue:
        u = queue.popleft()
        top_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # Step 4: Check for cycles
    if len(top_order) != len(in_degree):
        print("Graph has a cycle! Topological sorting not possible.")
    else:
        print("Topological Order:", top_order)


# Example graph (Directed Acyclic Graph - DAG)
graph = defaultdict(list)
graph[5] = [0, 2]
graph[4] = [0, 1]
graph[2] = [3]
graph[3] = [1]
graph[0] = []
graph[1] = []

# Run the function
topological_sort(graph)
