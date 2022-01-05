s = int(input())
n = 1
sum = 0
while 1:
    sum = sum + n
    if sum > s: 
        print(n-1)
        break
    n = n + 1