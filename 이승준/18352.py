import sys
from collections import deque
input=sys.stdin.readline
def bfs(graph,start):
    q=deque([start])
    while q:
        now=q.popleft()
        for next_node in graph[now]:
            if distance[next_node]==-1:
                distance[next_node]=distance[now]+1
                q.append(next_node)
    if K in distance:
        for i in range(1,N+1):
            if distance[i]==K:
                print(i)
    else:
        print(-1)
N,M,K,X=map(int,input().split())
distance=[-1]*(N+1)
distance[X]=0
graph=[[]for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
bfs(graph,X)


