N = int(input())
m = list(map(int, input().split()))
dp = [1] * N
k = N-1
while 1:
    if(k == 0):
        break
    for i in range(k):
        if(m[k]>m[i]):
            dp[i] = max(dp[i], dp[k]+1) 
    k = k-1
print(dp)
print(max(dp))

