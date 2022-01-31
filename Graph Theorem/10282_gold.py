import heapq


def dikstra(start):
    q = []
    dist = [INF]*(n+1)
    heapq.heappush(q,(start,0))
    dist[start] = 0

    while q:
        ni,wi = heapq.heappop(q)
        if(wi > dist[ni]):
            continue
        for nk,wk in graph[ni]:
            if(wk+wi < dist[nk]):
                dist[nk] = wk+wi
                heapq.heappush(q, (nk,wi+wk))
    count = 0
    for i in range(len(dist)):
        if(dist[i]==INF):
            dist[i] = -1
            continue
        count = count+1
    print(count, max(dist))

INF= 1e9
T = int(input())
for i in range(T):
    n,d,c = list(map(int, input().split()))
    graph = [[] for i in range(n+1)]
    for j in range(d):
        a,b,s = list(map(int, input().split()))
        graph[b].append((a,s))
    dikstra(c)

