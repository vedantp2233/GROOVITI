from collections import deque

def dfs(v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)

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

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = [[] for i in range(n)]

print("Enter edges:")

for i in range(e):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

start = int(input("Enter starting vertex: "))

print("\nDFS Traversal:")
visited = [False] * n
dfs(start, visited)

print("\nBFS Traversal:")
bfs(start)
