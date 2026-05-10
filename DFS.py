from collections import deque

# DFS Function
def dfs(v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)


# BFS Function
def bfs(start):
    visited = [False] * n
    queue = deque()

    visited[start] = True
    queue.append(start)

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


# Main Program

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

# Empty graph
graph = [[] for i in range(n)]

print("Enter edges:")

# Input edges
for i in range(e):
    u, v = map(int, input().split())

    # Undirected graph
    graph[u].append(v)
    graph[v].append(u)

start = int(input("Enter starting vertex: "))

# DFS
print("\nDFS Traversal:")
visited = [False] * n
dfs(start, visited)

# BFS
print("\nBFS Traversal:")
bfs(start)
