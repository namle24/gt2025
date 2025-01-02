from collections import defaultdict, deque

class node_graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def path_exists(self, start, end):
        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node == end:
                return True
            visited.add(node)
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

        return False


graph = node_graph()
edges = [
    (1, 2), (2, 5), (3, 6), (4, 6), (6, 7), (4, 7)
]

for u, v in edges:
    graph.add_edge(u, v)

start_node = int(input("Enter start node: "))
end_node = int(input("Enter end node: "))

if graph.path_exists(start_node, end_node):
    print("True")
else:
    print("False")
