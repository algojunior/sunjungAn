T = int(input())

idx = [[-2,1],[-1, 2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]] #8개의 방향


def dfs(visit, count, cur_pos, target_pos):
    x = cur_pos[0]
    y = cur_pos[1]
    if(x == target_pos[0] and y == target_pos[1]):
        print("방문")
        return count

    count = count + 1
    visit[y][x] = 1

    for i in range(8):
        new_x = x+idx[i][0]
        new_y = y+idx[i][1]
        if(0<=new_x<I and 0<=new_y<I and visit[y][x] == 0):
            dfs(visit, count, [new_x, new_y], target_pos)
        

for i in range(T):
    I = int(input())
    visit = [[0]*I for i in range(I)] #방문을 표기할 visit 배열
    cur_pos = list(map(int, input().split()))
    target_pos = list(map(int, input().split()))
    print(dfs(visit, 0, cur_pos, target_pos))
    
    
