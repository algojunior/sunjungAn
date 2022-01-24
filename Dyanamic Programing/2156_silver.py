N = int(input())
w = []
dp = [0] *(N+1)
w.append(0)
for i in range(N):
    w.append(int(input()))

dp[1] = w[1]
if(N == 1):
    print(dp[1])
    exit(0)

dp[2] = w[1]+w[2]
if(N==2):
    print(dp[2])
    exit(0)

for i in range(3, N+1):
    dp[i] = max(w[i]+dp[i-3]+w[i-1], w[i]+dp[i-2], dp[i-1])

print(dp[N])