import collections
idx_x = [-1, 1, 0, 0]
idx_y = [0, 0, -1, 1]

N, M = list(map(int, input().split()))
m = []
visit = []
flag = []
for i in range(N):
    m.append(list(map(int, input())))
    visit.append([1000]*M)
    flag.append([0]*M)

visit[0][0] = 0

def bfs(x, y):
    q = collections.deque()
    q.append([x,y])

    while q:
        x,y = q.popleft()
        if(x == M-1 and y == N-1):
            return

        for i in range(4):
            new_x = x+idx_x[i]
            new_y = y+idx_y[i]
            if(0<=new_x<M and 0<=new_y<N):
                if(m[new_y][new_x]==0): #벽이 아니면
                    if(flag[y][x] < flag[new_y][new_x]):
                        visit[new_y][new_x] = visit[y][x]+1
                        flag[new_y][new_x] = flag[y][x]
                        q.append([new_x, new_y])
                    elif(visit[new_y][new_x] > visit[y][x]+1):
                        visit[new_y][new_x] = visit[y][x]+1
                        flag[new_y][new_x] = flag[y][x]
                        q.append([new_x, new_y])
                    

                elif(flag[y][x]==0 and m[new_y][new_x]==1):
                    if(visit[new_y][new_x] > visit[y][x]+1):
                        visit[new_y][new_x] = visit[y][x]+1
                        flag[new_y][new_x] = 1
                        q.append([new_x, new_y])


        
bfs(0,0)
#print(flag)
#print(visit)
if(visit[N-1][M-1] == 1000):
    print(-1)
else:
    print(visit[N-1][M-1] + 1)


    

