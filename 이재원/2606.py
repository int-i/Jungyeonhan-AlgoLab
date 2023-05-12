
 인접 리스트로 그래프 구현
n = int(input())  # 컴퓨터의 개수
m = int(input())  # 연결된 쌍의 개수

graph = [[] for _ in range(n+1)]  # 1부터 n까지 인덱스를 사용하기 위해 n+1개의 빈 리스트를 만듦
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# DFS로 탐색하면서 바이러스에 감염된 컴퓨터의 수를 계산
def dfs(v, visited):
    visited[v] = True
    count = 1  # 현재 노드가 바이러스에 감염됨
    for i in graph[v]:
        if not visited[i]:
            count += dfs(i, visited)
    return count

visited = [False] * (n+1)
print(dfs(1, visited) - 1)  # 1번 컴퓨터는 바이러스에 감염되었으므로 제외해야 함
