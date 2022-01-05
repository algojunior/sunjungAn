import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
"""
메모리 초과
- N의 값이 100,000으로 2차원 배열을 사용하게 되면 메모리가 클 수 밖에 없음, 
값이 많이 들어가지도 않는데 초기 부터 큰 값을 넣어서 진행하면 메모리가 남아돔
--> 입접행렬 보다는 연결리스트로 충분히 구현 가능
"""
N = int(input())
visit = [0] * (N+1)
matrix = {} 
for i in range(N):
    matrix[i+1] = set()
for i in range(N-1):
    a, b = map(int, input().split(" "))
    matrix[a].add(b)
    matrix[b].add(a)
    
def dfs(V):
     #방문할 정점
    for i in matrix[V]: #연결되어 있고
        if visit[i] == 0: # 방문하지 않았으면
            visit[i] = V #부모노드 입력
            dfs(i)

dfs(1)

for i in range(2, len(visit)):
    print(visit[i])
