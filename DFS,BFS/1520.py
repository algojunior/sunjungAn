"""
<입력 형태>
세로의 크기 M
가로의 크기 N

<처리>
왼쪽 위부터, 오른쪽 맨 아래까지 이동하는데, 위로 가지는 못한다. 
이 상황에서, 몇가지 경로로 갈 수 있는지 counting

<입력 예제1>
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10

<답1>
3

<접근 방식>
DFS??
이동은 [0, 1], [0,-1] [1,0] [-1,0]이렇게 네가지임
50에서 갈 수 있는 것은 45, 35
backtraking 사용해야할 듯,,?


"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N , M = map(int, input().split(" "))
dst = [[0,1],[0,-1],[1,0],[-1,0]] #이동할 수 있도록

visit = [[-1] * M for i in range(N)]
table = []
for i in range(N): 
    table.append(list(map(int, input().split()))) 


def dfs(y,x):
    if y == N-1 and x == M-1: #오른쪽 맨 끝에 도착했다면
        return 1

    elif visit[y][x] != -1:
        return visit[y][x]

    else:
        visit[y][x] = 0
        for y_dst,x_dst in dst:
            new_y = y+y_dst
            new_x = x+x_dst
            if(new_y <N and new_x<M and new_y>=0 and new_x >=0):
                if(table[y][x]> table[new_y][new_x]): #낮은 곳만
                    visit[y][x] += dfs(new_y,new_x) 
        return visit[y][x]


print(dfs(0,0))





