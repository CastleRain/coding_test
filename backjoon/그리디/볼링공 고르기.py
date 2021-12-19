"""
볼링공 고르기

입력
5 3
1 3 2 3 2

출력
8

입력
8 5
1 5 4 3 2 4 5 2

출력
25
"""


# 시간복잡도가 매우 높은 문제풀이법이다.

# n, m = map(int, input().split())
# data = list(map(int, input().split()))
#
# count = 0
# # A가 도는 경우
# for i in range(n-1):
#
#     for j in  range(i+1, n):
#
#         # 무게가 다른경우
#         if data[i] != data[j]:
#             count += 1
#
# print(count)

