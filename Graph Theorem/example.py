import sys
from heapq import heappush,heappop
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    heap = []
    dis = [INF] * (n+1)
    heappush(heap,(0,start))
    dis[start] = 0
    
    while heap:
        weight,index = heappop(heap)
        if dis[index] < weight:
            continue
            
        for i in graph[index]:
            cost = weight + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heappush(heap,(cost,i[0]))
    return dis

n,e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(e):
    start,end,cost = map(int, input().split())
    graph[start].append((end,cost))
    graph[end].append((start,cost))

v1,v2 = map(int, input().split())
original_dis = dijkstra(1)
v1_dis = dijkstra(v1)
v2_dis = dijkstra(v2)

v1_path = original_dis[v1]+v1_dis[v2]+v2_dis[n]
v2_path = original_dis[v2]+v2_dis[v1]+v1_dis[n]
result = min(v1_path,v2_path)
print(result if result<INF else -1)
