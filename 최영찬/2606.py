from collections import deque
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
queue = deque([1])
visited[1] = True
count = 0
while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if not visited[neighbor]:
            queue.append(neighbor)
            visited[neighbor] = True
            count += 1
print(count)
