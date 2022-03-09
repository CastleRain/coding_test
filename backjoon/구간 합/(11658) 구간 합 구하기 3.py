"""
https://www.acmicpc.net/problem/11658

"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
sum_data = [[0] * (n+1) for i in range(n+1)]

update_data = [[] for i in range(n+1)]



# 1025 * 1025 = 약 100만
for i in range(1, n+1):
    for j in range(1, n+1):
        sum_data[i][j] = sum_data[i][j-1] + sum_data[i-1][j] - sum_data[i-1][j-1] + data[i-1][j-1]

# m = 10만 * 10만 = 약 100억번
for _ in range(m):
    i =  list(map(int, input().split()))
    if i[0] == 1:

        x1, y1, x2, y2 = i[1], i[2], i[3], i[4]
        result = sum_data[x2][y2] - sum_data[x1-1][y2] - sum_data[x2][y1-1] + sum_data[x1-1][y1-1]


        # 
        for x_num in range(x1, x2+1):
            for y_num, c  in update_data[x_num]:
                if y1 <= y_num <= y2:
                    result += c
        print(result)
    else:
        x1, y1, c = i[1], i[2], i[3]
        update_data[x1].append([y1, c - data[x1-1][y1-1]])


# 백준에선 numpy사용을 못한다.
# import sys
# import numpy as np

# input = sys.stdin.readline

# n, m = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(n)]
# sum_data = [[0] * (n+1) for i in range(n+1)]

# update_data = np.array([[0] * (n+1) for i in range(n+1)])



# # 1025 * 1025 = 약 100만
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         sum_data[i][j] = sum_data[i][j-1] + sum_data[i-1][j] - sum_data[i-1][j-1] + data[i-1][j-1]

# # m = 10만 * 10만 = 약 100억번
# for _ in range(m):
#     i =  list(map(int, input().split()))
#     if i[0] == 1:

#         x1, y1, x2, y2 = i[1], i[2], i[3], i[4]
#         result = sum_data[x2][y2] - sum_data[x1-1][y2] - sum_data[x2][y1-1] + sum_data[x1-1][y1-1] + update_data[x1:x2+1, y1: y2+1].sum()

#         print(result)
#     else:
#         x1, y1, c = i[1], i[2], i[3]
#         update_data[x1][y1] = c-data[x1-1][y1-1]





# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(n)]
# sum_data = [[0] * (n+1) for i in range(n+1)]

# update_data = [[] for i in range(n+1)]



# # 1025 * 1025 = 약 100만
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         sum_data[i][j] = sum_data[i][j-1] + sum_data[i-1][j] - sum_data[i-1][j-1] + data[i-1][j-1]

# # m = 10만 * 10만 = 약 100억번
# for _ in range(m):
#     i =  list(map(int, input().split()))
#     if i[0] == 1:

#         x1, y1, x2, y2 = i[1], i[2], i[3], i[4]
#         result = sum_data[x2][y2] - sum_data[x1-1][y2] - sum_data[x2][y1-1] + sum_data[x1-1][y1-1]


#         # 
#         for x_num in range(x1, x2+1):
#             for y_num, c  in update_data[x_num]:
#                 if y1 <= y_num <= y2:
#                     result += c
#         print(result)
#     else:
#         x1, y1, c = i[1], i[2], i[3]
#         update_data[x1].append([y1, c - data[x1-1][y1-1]])
