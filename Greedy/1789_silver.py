s = int(input())
n = 1
sum = 0
while 1:
    sum = sum + n
    if sum > s: 
        print(n-1)
        break
    n = n + 1



# 서로 다른 N개의 자연수의 합이 200라고 한다. 이때, 자연수 N의 최댓값은 얼마인가?