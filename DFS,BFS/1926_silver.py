import collections
N, M = list(map(int, input().split()))
p = []
idx_x = [-1,1, 0,0]
idx_y = [0,0,-1,1]

def dfs(y,x): #넓이도 같이 받음
    size = 0
    q = collections.deque()
    q.append([y,x])
    while(q):
        my,mx = q.popleft()
        if(p[my][mx] == 1 ):
            size = size+1
        p[my][mx] = 0
        for i in range(4):
            ny = my+idx_y[i]
            nx = mx+idx_x[i]
            if(0<=ny<N and 0<=nx<M):
                if(p[ny][nx] == 1):
                    q.append([ny,nx])
    return size



for i in range(N):
    p.append(list(map(int, input().split())))

arr = []
for i in range(N):
    for j in range(M):
        if(p[i][j] == 1):
            arr.append(dfs(i,j))
    
print(len(arr))
print(max(arr))
        
