import heapq

V, E = list(map(int, input().split()))
dist = [11]*(V+1) 
graph = [[] for i in range(V+1)]
K = int(input())
for i in range(E):
    u,v,w = list(map(int, input().split()))
    graph[u].append((v,w))
    
start = K
q = []
heapq.heappush(q,(start,0))
dist[start] = 0

while q:
    ni, wi = heapq.heappop(q)

    if dist[ni] < wi:
        continue
    for nk,wk in graph[ni]:
        if wi+wk < dist[nk]:
            dist[nk] = wi+wk
            heapq.heappush(q,(nk, dist[nk]))

for k in range(1,len(dist)):
    if(dist[k] == 11):
        print('INF')
    else: print(dist[k])
    
