N, M, V = map(int, input().split())
matrix = [[0] * (N+1) for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1 #서로가 연결 되어 있음을 표시해줌
visit_list = [0]*(N+1)

def dfs(V): #깊이 우선 탐색
    visit_list[V] = 1 #방문한 점 1로 표시
    print(V, end=' ')
    for i in range(1, N+1):
        if(visit_list[i] == 0 and matrix[V][i] == 1):
            dfs(i)


def bfs(V): #넓이 우선 탐색
    queue=[V] #들려야할 정점 저장
    visit_list[V] = 0 #방문한 점 0으로 표시
    while queue:
        V = queue.pop(0)
        print(V, end= ' ')
        for i in range(1, N+1):
            if(visit_list[i] == 1 and matrix[V][i] == 1):
                queue.append(i)
                visit_list[i] = 0

dfs(V) #dfs 실행
bfs(V) #bfs 실행

""" dfs는 재귀적인 구현, bfs는 반복문의 의한 구현"""