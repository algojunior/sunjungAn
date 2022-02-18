import sys 
input = sys.stdin.readline


N = int(input())
arr = [1,2]
for i in range(3, N+1):
    arr.append((arr[i-3]+arr[i-2])%15746)
    
print(arr[N-1])