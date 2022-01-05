arr = []
brr = []
arr = list(input())
for w in arr:
    brr.append(int(w))

sum = sum(brr)
if(0 not in brr):
    print(-1)
    
# 가장 큰 수대로 반복문 돌리기
# 30의 배수는 마지막 숫자가 0이고, 나머지 숫자가 3의 배수여야함
# 3의 배수 특징은 모든 수에서 자리수를 각각 더해서 3의 배수가 되면 그 수는 3의 배수이다. 
# 따라서 위의 특징을 만족시키는 수에서 가장 큰 수를 반환하면 됨


elif(sum % 3) != 0:
    print(-1)

else: 
    brr.sort()
    brr.reverse()
    for b in brr:
        print(b, end="")
    



