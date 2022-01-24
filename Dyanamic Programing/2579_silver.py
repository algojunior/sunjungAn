st = int(input())
w = []
for i in range(st):
    v = int(input())
    w.append(v)
flag = 0
k =0
while 1:
    if(k+1>= st or k+2>=st):
        break
    if(w[k+1]<w[k+2]): #두 칸 뛰는게 유리하다면
        w[k+2] = w[k] + w[k+2]
        k = k+2
        flag = 0
    elif(flag == 1):
        w[k+2] = w[k] + w[k+2]
        k = k+2
        flag = 0
    else:
        w[k+1] = w[k] + w[k+1]
        k = k+1
        flag = 1

if(len(w)== 0):
    print(0)
elif(len(w) == 1):
    print(w[0])
elif(w[st-1] < w[st-2]):
    print(w[st-1] + w[st-2])
else:
    print(w[st-1])
#print(w)


