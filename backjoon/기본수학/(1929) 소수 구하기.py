"""
https://www.acmicpc.net/problem/1929

"""
import math
n, m = map(int, input().split())

dp = [-1] * (m + 1)
dp[1] = 2

for k in range(4, m+1, 2):
    dp[k] = 2


for i in range(n, m+1):

    # 만약 i가 소수면 i의 2배는 다 2로 만들자.
    
    # 처음 들어오거나 이전에 구한 소수에서 나온 수가 아니면 소수 판별에 들어간다.
    if dp[i] == -1:
        flag = 0
        for l in range(2, int(math.sqrt(i))+1):
            if i % l == 0:
                flag = 1
                break
        
        if flag == 0:
            print(i)
            for a in range(i, m+1, i*2):
                dp[a] = 2

