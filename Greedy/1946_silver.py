"""
<입력>
첫째 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 20)가 주어진다.
각 테스트 케이스의 첫째 줄에 지원자의 숫자 N(1 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N개 줄에는 각각의 지원자의 서류심사 성적, 면접 성적의 순위가 공백을 사이에 두고 한 줄에 주어진다. 
두 성적 순위는 모두 1위부터 N위까지 동석차 없이 결정된다고 가정한다.
"""

T = int(input()) #테스트 케이스 수
for i in range (T):
    answer = 0
    vol = int(input()) #면접
    s = [0]*vol
    for j in range(vol): #입력 다 받는 중
        num1, num2 = input().split(" ")
        s[int(num1)-1] = int(num2) #정렬 역할

    iter = vol
    while 1:
        refer = s[0] #기준 값
        pos = 0
        answer = answer + 1
        for k in range(1, iter):
            if refer > s[k]:
                s[pos] = s[k]
                pos = pos+1
        iter = pos
        if iter == 1:
            print(answer+1)
            break
                
        
"""
<예시 1>
5
3 2
1 4
4 1
2 3
5 5

(3 2) 입장에서는 없음
(1 4) 입장에서도 없음
(4 1) 입장에서도 없음
(2 3) 입장에서도 없음
(5 5) 입장에서는 모두가 자기보다 앞섬

<예시 2>
7
3 6 -> X
7 3 -> X
4 2 -> O
1 4 -> O
5 7 -> X
2 5 -> X
6 1 -> O

<접근 방식>
1 2 3 4 5 6 7
4 5 6 2 7 1 3
O X X > X > >

1 2 3
2 1 3
O > X

>> 이 방식이 배열의 요소가 하나 남았을 때 종료
"""