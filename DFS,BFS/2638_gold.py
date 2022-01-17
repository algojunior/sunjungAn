import collections
import sys
input = sys.stdin.readline

def check_cheese(y,x):
    qe = collections.deque()
    qe.append([y,x])
    while(qe):
        y,x = qe.popleft()
        m[y][x] = 2
        for i in range(4):
            ny = y+idx_y[i]
            nx = x+idx_x[i]
            if(0<=ny<N and 0<=nx<M):
                if(m[ny][nx] == 0):
                    qe.append([ny, nx])

N, M = list(map(int, input().split()))

idx_x = [-1,1,0,0]
idx_y = [0,0,-1,1]

q = collections.deque()
m = []
ans = 0
for i in range(N):
    arr = (list(map(int, input().split())))
    m.append(arr)
    for j in range(M):
        if(arr[j] == 1):
            q.append([i,j])
                
it = len(q)
arr = []
check_cheese(0,0)

while(q):
    y,x = q.popleft()
    it = it-1
    count = 0
    for i in range(4):
        ny = y+idx_y[i]
        nx = x+idx_x[i]
        if(0<=nx<M and 0<=ny<N):
            if(m[ny][nx] == 2):
                count = count+1

    if(count >= 2):
        arr.append([y,x])

    else: q.append([y,x])

    if(it == 0):
        ans = ans +1
        it = len(q)
        for y, x in (arr):
            m[y][x] = 2
            check_cheese(y,x)

print(ans)


    




