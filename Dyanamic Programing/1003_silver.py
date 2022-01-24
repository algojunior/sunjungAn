T = int(input())
fibo = [[1,0],[0,1],[1,1],[1,2]]

for i in range(T):
    c = int(input())
    if c < len(fibo):
        print(fibo[c][0],fibo[c][1])
    else: 
        l = len(fibo)
        for j in range(l,c+1):
            fibo.append([fibo[j-1][0] + fibo[j-2][0], fibo[j-1][1] + fibo[j-2][1]])
        print(fibo[c][0],fibo[c][1])  

        



