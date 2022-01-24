t = int(input())
w = list(map(int, input().split()))
v = [0]*(t+1)

prev = 0
for k in range(t):
    v[k] = prev+w[k]
    if(prev > w[k]):
        print(prev)
        prev = 0
    else: prev = v[k]

print(v)
if(prev == 0):
    print(max(w))
else: print(max(v))
 