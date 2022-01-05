n = int(input())

# 한 줄 하나의 배열로 나타내기
arr = []
brr = []
for w in input().split():
    arr.append(int(w))

for w in input().split():
    brr.append(int(w))

arr.sort()
brr.sort()

sum = 0
for i in range(n):
    sum = sum + (arr[i]* brr[n-1-i])

print(sum)
    
