import sys
import collections

sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input())

idx = [[-2,1],[-1, 2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]] #8개의 방향


def dfs(count, cur_pos, target_pos):
    visit[cur_pos[1]][cur_pos[0]] = 0
    #print("count: ",count)
    deq.append(cur_pos)
    while deq:
        x, y = deq.popleft()

        if(x == target_pos[0] and y == target_pos[1]):
            return visit[y][x]

        for i in range(8):
            new_x = x+idx[i][0]
            new_y = y+idx[i][1]
            if(0<=new_x<I and 0<=new_y<I and visit[new_y][new_x] == 0):
                deq.append([new_x, new_y])
                visit[new_y][new_x] = visit[y][x] + 1
        
        

for i in range(T):
    I = int(input())
    visit = [[0]*I for i in range(I)] #방문을 표기할 visit 배열
    cur_pos = list(map(int, input().split()))
    target_pos = list(map(int, input().split()))
    deq = collections.deque()
    print(dfs( 0, cur_pos, target_pos))
    
    
