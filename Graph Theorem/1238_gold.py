import heapq
INF = 1e9
N, M, X = list(map(int, input().split()))
graph = [[] for i in range(N+1)]
for i in range(M):
    a,b,c = list(map(int, input().split()))
    graph[a].append((b,c))

def dikstra(start):
    q = []
    dist = [INF]*(N+1)
    heapq.heappush(q,(start, 0))

    while q:
        ni, wi = heapq.heappop(q)
        if(wi > dist[ni]):
            continue
        for nk, wk in graph[ni]:
            if(wk+wi < dist[nk]):
                dist[nk] = wk+wi
                heapq.heappush(q,(nk,wk+wi))
    return dist
    
xto_dist = dikstra(X)
m = 0
for i in range(1,N+1):
    if(i == X):
        continue
    i_dist = dikstra(i)
    if(m < i_dist[X] + xto_dist[i]):
        m = i_dist[X]+xto_dist[i]

print(m)
