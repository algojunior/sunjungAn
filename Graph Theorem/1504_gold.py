import heapq
INF = int(1e9)
N,E = list(map(int, input().split()))
graph = [[] for i in range(N+1)]
for i in range(E):
    a,b,c = list(map(int, input().split()))
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2 = list(map(int, input().split())) #반드시 거쳐야 하는 정점

def dikstra(start):
    dist = [INF]*(N+1)
    q = []
    heapq.heappush(q,(start,0))
    dist[start] = 0
    while q:
        now, weight = heapq.heappop(q)
        if(weight > dist[now]):
            continue
        for nk, wk in graph[now]:
            if(wk+weight < dist[nk]):
                heapq.heappush(q,(nk,wk+weight))
                dist[nk] = wk+weight

    return dist

dist1 = dikstra(1)
dist2 = dikstra(v1)
dist3 = dikstra(v2)

#경로 1 (0 -> v1 -> v2 -> N)
path1 = dist1[v1] + dist2[v2] + dist3[N]
path2 = dist1[v2] + dist3[v1] + dist2[N]


m = min(path1, path2)
if(m > INF):
    print(-1)
else: print(m)