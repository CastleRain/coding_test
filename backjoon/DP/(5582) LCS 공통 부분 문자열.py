"""
LCS (longest common substring)
공통 부분 문자열
"""

"""
풀이방법 : 
1. dp[i][j] 행렬을 만든다.
2. for문을 돌리며 data[i] == data2[j]의 값을 비교한다.
3. 만약 같을 시 dp[i-1][j-2] + 1 값을 출력해준다. (이전값 +1)
"""




# 시간초과
n = input()
m = input()

result = 0

# 2줄을 계속 이용한다.
dp = [[0] * (len(m)+1) for _ in range(2)]
n = " " + n
m = " " + m

for i in range(1, len(n)):
    if i != 0:
        dp[0] = dp[1]
        dp[1] = [0] * len(m)

    for j in range(1, len(m)):
        i_index = 1

        if n[i] == m[j]:
            dp[i_index][j] = dp[i_index-1][j-1] + 1

        result = max(result, dp[i_index][j])

print(result)


# 메모리 부족뜸
# n = input()
# m = input()
#
# dp = [[0] * (len(m)+1) for _ in range(len(n)+1)]
# n = " " + n
# m = " " + m
# result = 0
# for i in range(len(n)):
#
#     for j in range(len(m)):
#
#         if i == 0 or j == 0:
#             dp[i][j] = 0
#         elif n[i] == m[j]:
#             dp[i][j] = dp[i-1][j-1] + 1
#
#         result = max(result, dp[i][j])
#
# print(result)
