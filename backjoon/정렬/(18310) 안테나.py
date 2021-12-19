"""
안테나

https://www.acmicpc.net/problem/18310
집 위에만 설치가 가능하다.

중복된 집은
"""

import sys
input = sys.stdin.readline


# 이진 탐색 리스트, 찾아야하는 데이터, left, right)
# def binary_search(list, target, left, right):
#
#     if left > right:
#         return None
#
#     mid = (left + right) // 2
#
#     if list[mid] == target:
#         return mid
#     # 현재 타겟보다 작은경우
#     elif list[mid] < target:
#         return binary_search(list, target, mid+1, right)
#
#     # 타겟보다 큰경우
#     else:
#         return binary_search(list, target, left, mid-1)


n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n-1)//2])




