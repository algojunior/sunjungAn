"""
https://www.acmicpc.net/problem/14501
"""
N = int(input())
T = []
P = []
visit = [0]*(N+1)
for i in range(N):
    t, p = list(map(int, input().split()))
    T.append(t)
    P.append(p)

for i in range(N):
    if T[i]+i <= N:
        visit[i] = visit[i] + P[i]

        for k in range(T[i]+i, N):
            visit[k] = max(visit[k], visit[i])

print(max(visit))

