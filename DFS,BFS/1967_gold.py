N = int(input())
parent = [0]*(N+1) #부모 저장
w = [0]*(N+1) #간선 저장
answer = [[] for i in range(N+1)]

for i in range(N-1):
    p, c, wk = list(map(int, input().split()))
    parent[c] = p
    w[c] = wk #c와 p의 연결고리


for i in range(N):
    # N부터
    idx = N-i
    if(idx == 1):
        break
    #print(w[idx])
    if(len(answer[idx]) == 0): #자식이 아무 것도 없다면
        answer[parent[idx]].append(w[idx]) #그냥 부모에 추가
    elif(len(answer[idx]) == 1): #자식이 하나 있다면
        #print(answer[parent[idx]][0])
        answer[parent[idx]].append(w[idx]+answer[idx][0])
    else: #두개 있다면
        m = max(answer[idx])
        answer[parent[idx]].append(w[idx]+m)

arr = []
print(answer)
for i in range(N):
    if(len(answer[i])>2): #2개보다 크면 2개로 추려야함
        answer[i].sort()
        arr.append(answer[i][len(answer[i])-1]+ answer[i][len(answer[i])-2])
    else: arr.append(sum(answer[i]))

print(max(arr))
    

    



    
