city = int(input())

dst = input().split(" ")
node = input().split(" ")[:-1]
answer = 0

while 1 :
    if len(node) == 1:
        print(answer + int(node[0])*int(dst[0]))
        break
    if len(node) == 0:
        print(answer)
        break
    m = min(node) #가장 작은 값 찾기
    idx = node.index(m) # 가장 작은 값에서 가장 왼쪽에 있는 값 찾기
    sum_dst = 0
    for i in range(idx, len(dst)): # idx보다 뒤에 거리가 얼마나 있는지
        sum_dst = sum_dst + int(dst[i])
    answer = answer + (sum_dst * int(m))
    node = node[:idx]
    dst = dst[:idx]


        
"""
<예제>
4
2 3 1
5 2 4 1

총 건너야할 거리 = 2 + 3 + 1 = 6

가장 적은 도시에서 최대한 많이!
두번째 도시에서 한번에 가기! -> 2*(3 + 1) = 8
두번째 도시 이후는 더이상 신경 쓰지 않음
두번째보다 앞에 있는 도시에서 최소한의 거리만 결제


<접근 방법>
마지막 도시를 제외하고, 각각의 거리와 도시들을 짝으로 하는 데이터를 만듬 -> 이때, 값이 중복을 허락하므로 일반적인 리스트로는 구현 불가

"""

""" 17점 통과일 때, 예외 사례 
5
3 5 3 4 
5 2 4 1 1

-> (1 * 4) + (2 * 8) + (5 * 3) = 4 + 16 + 15 = 35

"""
""" 58점 통과일 때 
시간을 줄이자!
"""