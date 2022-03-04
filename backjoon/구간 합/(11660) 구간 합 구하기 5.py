"""
https://www.acmicpc.net/problem/11660

누적합 배열을 이용해보자.

2차원 그래프이므로 행 -> 열 순서로 더해주자..

(1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000) 
100,000,000 => 1초
"""
# dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j] - dp[i][j]) + s[i][j]


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
sum_data = [[0] * (n+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        sum_data[i][j] = sum_data[i][j-1] + sum_data[i-1][j] - sum_data[i-1][j-1] + data[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    print(sum_data[x2][y2] - sum_data[x1-1][y2] - sum_data[x2][y1-1] + sum_data[x1-1][y1-1])





# # 행 합 => m*n
# for i in range(n):
#     sum_data = 0
#     for d in list(map(int, input().split())):
#         sum_data += d
#         data[i].append(sum_data)
# # 열 합

# for i in range(1, len(data)): # 2행부터 읽어온다.
#     for j in range(len(data)): # 열을 바꾸어가며 더해간다.
#         data[i][j] += data[i-1][j]

# # x1 <= x2 , y1 <= y2
# def prefix_sum(x1,y1, x2, y2, data):
#     sum  = 0
#     # 제일 큰 바깥 사각형을 계산
#     sum += data[x2][y2]

#     # 왼쪽 사각형 계산 (0보다 작아지게되면 패스)
#     if x1-1 >= 0:
#         sum -= data[x1-1][y2]
#     if y1 - 1 >= 0:
#         sum -= data[x2][y1-1]
#     if x1-1 >= 0 and y1-1>= 0:
#         sum += data[x1-1][y1-1]


#     return sum
# for _ in range(m):
#     x1, y1, x2, y2 = map(int, input().split())
#     print(prefix_sum(x1-1, y1-1,x2-1,y2-1, data))





# # python : 시간초과
# # pypy : 시간초과
# n, m = map(int, input().split())
# data = [[] for _ in range(n+1)]

# # 행 합 => m*n
# for i in range(n):
#     sum_data = 0
#     for d in list(map(int, input().split())):
#         sum_data += d
#         data[i].append(sum_data)
# # 열 합

# for i in range(1, len(data)): # 2행부터 읽어온다.
#     for j in range(len(data)): # 열을 바꾸어가며 더해간다.
#         data[i][j] += data[i-1][j]

# # x1 <= x2 , y1 <= y2
# def prefix_sum(x1,y1, x2, y2, data):
#     sum  = 0
#     # 제일 큰 바깥 사각형을 계산
#     sum += data[x2][y2]

#     # 왼쪽 사각형 계산 (0보다 작아지게되면 패스)
#     if x1-1 >= 0:
#         sum -= data[x1-1][y2]
#     if y1 - 1 >= 0:
#         sum -= data[x2][y1-1]
#     if x1-1 >= 0 and y1-1>= 0:
#         sum += data[x1-1][y1-1]


#     return sum
# for _ in range(m):
#     x1, y1, x2, y2 = map(int, input().split())
#     print(prefix_sum(x1-1, y1-1,x2-1,y2-1, data))
