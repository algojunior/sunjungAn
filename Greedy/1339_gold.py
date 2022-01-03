"""
<문제 요약>
입력: 첫째 줄에 단어의 개수N
    둘째 줄에 N개의 줄에 단어가 한 줄에 하나씩 주어짐(대문자로만)
    (단, 모든 단어에 포함되어 있는 알파벳은 최대 10개, 수의 최대 길이는 8개, 서로 다른 문자는 서로 다른 숫자를 나타냄)
처리: 각 대문자를 0~9로 바꿈 -> N개의 수를 합함
ex) GCF + ACDEB,  A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정하면 99437이 최대
"""

"""
<예제 분석1>
2
GCF
ACDEB

A, C, (D+G), (E+C), (B+F)
제일 커야하는 우선순위는.. A > C > D+G > E+C > B+F
1. A에 9를 부여
2. C에 8를 부여
3. D와 G중에 빈도수가 많은 것에 더 큰값을 줌 -> 둘다 하나씩 밖에 없으므로, D는 7, G는 6
4. E에 5부여
5. B와 F중에 빈도수가 많은 것에 더 큰값을 줌 -> 둘다 하나씩 밖에 없으므로, B는 4, F는 3

<예제 분석2>
2
GCG
ACD

(G+A), (C+C), (D+G)
제일 거야 하는 우선순위는 (G+A) > (C+C) > (D+G)
1. A와 G중에 빈도수가 많은 것에 더 큰 값을 줌 -> G가 더 많으므로, G=9, A=8
2. C는 7
3. D는 6

<접근 방식>
GCG
ACD

우선 순위의 대한 점수를 파악한다. 
1. 입력 받으면서 빈도수 체크
G = 2, C = 2, A = 1, D = 1
2. 위치 정보 입력 받기
가장 최근 왼쪽에 있는 위치 -> len(arr) - arr.index('G') = 3 (가중치)
-> len(brr) - brr.index('C') = 2  
위치 정보가 제일 중요하니까 위치 가중치에다 * 100 해주면 될듯

따라서 위의 예시에서는,
A = 300 + 1
C = 200 + 2 --> 두 번째 C를 만날때, 계산한 값이랑 비교해서 더 큰값을 넣기
D = 100 + 1
G = 300 + 2

--> 큰 값부터 9를 넣음
"""

N = int(input())
s =[]
m = [0]*30
v = [0]*30
for i in range(N):
    s.append(input())
for str in s:
    for alpha in str:
        #m[ord(alpha)-65] = m[ord(alpha)-65] + 1 #알파벳 빈도수 증가
        v[ord(alpha)-65] = v[ord(alpha)-65] + (10**(len(str) - str.index(alpha))) #가중치 계산
        swap = str[str.index(alpha)+1:]
        str = swap
        #if value > v[ord(alpha)-65]: #이전 값보다 크면 값을 바꿈
        #    v[ord(alpha) -65] = value

#print(v)
#모든 알파벳 들의 위치, 빈도수 정보가 다 들어가 있는 상태

num = 9
while 1: # 0~9값을 부여
    maximum = max(v)
    if maximum < 10:
        break
    max_idx = v.index(maximum)
    v[max_idx] = num #가장 큰 값 부여
    num = num -1 

# v배열에는 이제 0~9사이의 값들만 존재
#print(v)

answer = []
for str in s:
    length = len(str) #3이면
    a = 0
    for alpha in str:
        a = a + v[ord(alpha)-65]*(10**(length-1))
        length = length - 1
    answer.append(a)
#print(v)
print(sum(answer))

    

        
        


    
    