""" 
<입력>
1. 테스트 케이스 개수K
2. 정점의 개수 V, 간선의 개수 E
3. E개의 (u,v) 간선의 정보

<출력> 
각 테스트 케이스에 대해서 이분 그래프이면, YES 아니면 NO

<입력 예제 1>
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2

YES
NO

<접근 방법>
이분 그래프: 인접한 정점끼리 서로 다른 색으로 칠해서 모든 정점을 두 가지 색으로만 칠할 수 있는 그래프.

즉 이분 그래프는 항상 인접한 그래프는 같은 색일 수가 없다!
하나라도 인접한 정점이 같은 색이라면 이것은 이분 그래프가 아니다. 

"""

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


def bfs(v, matrix, visit):
    queue = []
    while 1:
        if(visit[v] ==1):
            h = -1
        else: h = 1

        if(len(matrix[v]) == 0):
            visit[v] = h
        
        else:
            for vh in matrix[v]:
                if(visit[vh]==0): #방문 여부가 0이면 아직 방문 안함
                    visit[vh] = h
                    queue.append(vh)
                elif(visit[vh] == visit[v]): #하나라도 겹친다면
                    return -1
                else: #겹치지 않는다면
                    continue
        
        if(len(queue)==0):
            if 0 in visit:
                queue.append(visit.index(0))
                #print(visit.index(0))
            else: return 1
        
        #print(queue)
        v= queue.pop()

K = int(input())

for i in range(K):
    V, U = map(int, input().split())
    visit = [0]*(V+1)
    visit[0] = -2
    visit[1] = 1
    matrix = {}

    for m in range(1, V+1):
        matrix[m] =set()

    for j in range(U):
        a, b = map(int, input().split())
        if(a == b):
            continue
        matrix[a].add(b)
        matrix[b].add(a)
    
    answer = bfs(1,matrix, visit)
    #print(visit)
    #print(answer)
    if answer == -1:
        print('NO')
    else: print('YES')


            
            

