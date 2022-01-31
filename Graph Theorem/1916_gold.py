import heapq
import sys
input = sys.stdin.readline

N = int(input()) #노드
M = int(input()) #간선 
graph = [[] for i in range(N+1)]
for i in range(M):
    s, e, w = list(map(int, input().split()))
    graph[s].append((e,w))


start, end = list(map(int, input().split()))
q = []
dist = [100001] * (N+1)
heapq.heappush(q, (start,0)) #시작점과 0(거리)를 줌
dist[start] = 0

while q:
    now, weight = heapq.heappop(q)
    if(weight>dist[now]):
        continue
    for nk,wk in graph[now]:
        if(wk+weight < dist[nk]):
            heapq.heappush(q,(nk,wk+weight))
            dist[nk] = wk+weight

print(dist[end])

    
