import heapq

def create_weighted_adjacency_matrix():
    n = 9
    adj_matrix = [[0] * n for _ in range(n)]
    edges = [
        (1, 2, 4), (1, 5, 1), (1, 7, 2),
        (2, 3, 7), (2, 6, 5),
        (3, 4, 1), (3, 6, 8),
        (4, 6, 6), (4, 7, 4), (4, 8, 3),
        (5, 6, 9), (5, 7, 10),
        (6, 9, 2),
        (7, 9, 8),
        (8, 9, 1),
        (9, 8, 7)
    ]
    for u, v, w in edges:
        adj_matrix[u-1][v-1] = w
        adj_matrix[v-1][u-1] = w
    return adj_matrix

def print_adjacency_matrix(adj_matrix):
    for row in adj_matrix:
        print(" ".join(f"{x:2}" for x in row))

def prim_mst(adj_matrix, root):
    n = len(adj_matrix)
    visited = [False] * n
    min_heap = [(0, root, -1)]
    mst_edges = []
    total_weight = 0
    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)
        if visited[node]:
            continue
        visited[node] = True
        total_weight += weight
        if parent != -1:
            mst_edges.append((parent + 1, node + 1, weight))
        for neighbor in range(n):
            if not visited[neighbor] and adj_matrix[node][neighbor] > 0:
                heapq.heappush(min_heap, (adj_matrix[node][neighbor], neighbor, node))
    return mst_edges, total_weight

def kruskal_mst(adj_matrix):
    n = len(adj_matrix)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if adj_matrix[i][j] > 0:
                edges.append((adj_matrix[i][j], i, j))
    edges.sort()
    parent = list(range(n))
    rank = [0] * n
    mst_edges = []
    total_weight = 0
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u + 1, v + 1, weight))
            total_weight += weight
    return mst_edges, total_weight

if __name__ == "__main__":
    adj_matrix = create_weighted_adjacency_matrix()
    print_adjacency_matrix(adj_matrix)
    root_node = int(input("\nEnter the root node (1-9): ")) - 1
    print("\nPrim's Algorithm:")
    prim_edges, prim_weight = prim_mst(adj_matrix, root_node)
    print("Edges in MST:", prim_edges)
    print("Total Weight of MST:", prim_weight)
    print("\nKruskal's Algorithm:")
    kruskal_edges, kruskal_weight = kruskal_mst(adj_matrix)
    print("Edges in MST:", kruskal_edges)
    print("Total Weight of MST:", kruskal_weight)
