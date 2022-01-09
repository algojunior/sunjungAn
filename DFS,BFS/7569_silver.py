"""
<입력>
상자 크기: M(가로) X N(세로)
상자의 수 : H

<처리>
하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 (6방향)
익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수

"""
import sys
M, N, H = list(map(int, input().split(" ")))
tomato = [[list(map(int, sys.stdin.readline().split())) for i in range(N)] for j in range(H)] #3차원
idx_x = [-1, 1, 0, 0, 0, 0 ]
idx_y = [0, 0, -1, 1, 0, 0 ]
idx_z = [0, 0, 0, 0, -1, 1 ]
queue = []

for h in range(H):
    for n in range(N):
        for m in range(M):
            if(tomato[h][n][m]==1):
                queue.append([h, n, m]) # 익은 토마토가 있는 높이, 열, 행

    
count = 0
queue_len = len(queue) #익은 토마토 개수
if queue_len != 0:
    while 1:
        pos = queue.pop(0)
        queue_len = queue_len - 1
        for i in range(6):
            new_h = pos[0] + idx_z[i]
            new_y = pos[1] + idx_y[i]
            new_x = pos[2] + idx_x[i]
            if(0<=new_h<H and 0<=new_y<N and 0<=new_x<M and tomato[new_h][new_y][new_x] == 0):
                queue.append([new_h, new_y, new_x])
                tomato[new_h][new_y][new_x] = 1

        if (queue_len == 0):
            queue_len = len(queue)          
            if(queue_len == 0):
                break
            else: 
                count = count + 1

            

    
answer = count
for h in range(H):
    for n in range(N):
        for m in range(M):
            if 0 == tomato[h][n][m]:
                print(-1)
                exit()

print(answer)


    
    





