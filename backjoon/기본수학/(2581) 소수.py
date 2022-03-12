"""

https://www.acmicpc.net/problem/2581

소수판별을 진행,

2의배수 제거

"""

# 1만개의 데이터 저장
dp = [0] * 10001

dp[1] = 1

max_len = 10000

# 2부터 올라가면서 소수
for i in range(2,max_len+1):
    if dp[i] == 0:
        dp[i] = 2

        first_i = i * 2
        for j in range(first_i, max_len+1, i):
            dp[j] = 1

m = int(input())
n = int(input())

result = []
for i in range(m, n+1):
    if dp[i] == 2:
        result.append(i)

if len(result) != 0:

    print(sum(result))
    print(result[0])
else:
    print("-1")