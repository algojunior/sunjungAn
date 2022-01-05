#메모리 초과 코드
N = int(input())
visit = [0] * (N+1)
matrix = [[0]*(N+1) for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split(" "))
    matrix[a][b] = matrix[b][a] = 1
    
def dfs(V):
     #방문할 정점
    for i in range(1,N+1):
        if matrix[V][i] == 1 and visit[i] == 0: #연결되어 있고, 방문하지 않았으면
            visit[i] = V #부모노드 입력
            dfs(i)
        
dfs(1)

for i in range(2, len(visit)):
    print(visit[i])

""" 
<예제 입력2>
12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12

1 2 3 4 5 6 7 8 9 10 11 12 
  1 1 

1 -> 2 3
2 -> 4 1
3 -> 5 6 1
4 -> 7 8 2
5 -> 9 10 3
6 -> 11 12 3
"""

