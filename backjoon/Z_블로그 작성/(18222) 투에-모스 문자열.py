"""
문제 링크 : https://www.acmicpc.net/problem/18222
푼 날짜 : 220311
문제 유형 : 분할 정복


풀이 : 
X는 맨 처음에 "0"으로 시작한다. 
X에서 0을 1로, 1을 0으로 뒤바꾼 문자열 X'을 만든다.
X의 뒤에 X'를 붙인 문자열을 X로 다시 정의한다. 
2~3의 과정을 무한히 반복한다.

k의 범위가 10^18이다.


계속 숫자를보다 안게 2^n마다 0 1이 바뀐다

승
0   0
1   1
2   0
3   1
4   0
5   1
6   0

1. 처음 시작이 0으로 시작을 하니 해당 k가 몇번째에 속하는지 확인을 하고
2. 그전 단계까지 다시 자른뒤 2^0을 계산하고
3. 다시 1, 2를 반복해서 끝까지가면 나온다.

ex 31
1. -> 32 (2^5) = 0
2. 2^4 = 1
3. 2^4 ~ 2^5까지 나눈 뒤 다시 해당 값 (n-2^4) 의 위치 확인

if 2^0 까지 오면 해당 값 출력


"""

import sys
import math

def solution(n, k):

    if n == 1:
        print(k) 
        exit(0)

    num = math.log(n, 2)
    if num-int(num) == 0: # 완벽히 나누어 떨어지는 경우
        if num % 2 == 0:
            print(k)
            exit(0)
        else:
            print((k+1)%2)
            exit(0)
        
    else:
        num = int(num)


    if num % 2 == 0:
        
        solution(n-2**num, (k+1)%2)
    else:
        k = (k+1) % 2
        solution(n-2**num, k)

if __name__ == "__main__":
    n = int(input())
    solution(n, 0)
        