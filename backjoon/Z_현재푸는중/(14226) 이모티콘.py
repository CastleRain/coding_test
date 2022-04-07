"""
문제 링크 : https://www.acmicpc.net/problem/14226
푼 날짜 : 220325
문제 유형 : DP


풀이 : 


"""

# from collections import deque
# n = int(input())
# dist = [[-1]* (n+1) for _ in range(n+1)]
# q = deque()
# q.append((1,0))  # 화면 이모티콘 개수, 클립보드 이모티콘 개수
# dist[1][0] = 0
# while q:
#     s,c = q.popleft()
#     if dist[s][s] == -1: # 방문하지 않았으면
#         dist[s][s] = dist[s][c] + 1
#         q.append((s,s))
#     if s+c <= n and dist[s+c][c] == -1:
#         dist[s+c][c] = dist[s][c] + 1
#         q.append((s+c, c))
#     if s-1 >= 0 and dist[s-1][c] == -1:
#         dist[s-1][c] = dist[s][c] + 1
#         q.append((s-1, c))
# answer = -1
# for i in range(n+1):
#     if dist[n][i] != -1:
#         if answer == -1 or answer > dist[n][i]:
#             answer = dist[n][i]
# print(answer)



import sys

n = int(input())

max_num = 3000

dp = [0] * max_num

for i in range(1, max_num):
    dp[i] = i


for i in range(2, max_num-1):
    dp[i] = min(dp[i+1]+1, dp[i])

    for j in range(2*i, max_num-1, i):
        if j == 2*i: #처음값일 땐
            dp[j] = min(dp[j], dp[j-i]+2, dp[j+1] + 1) # 복 붙
        else:
            dp[j] = min(dp[j], dp[j-i]+1, dp[j+1]+1) # 붙


print(dp[n])

        
# for i in range(2, max_num-1):
#     dp[i] = min(dp[i+1] + 1, dp[i])

