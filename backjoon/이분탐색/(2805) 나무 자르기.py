"""
나무 자르기

https://www.acmicpc.net/problem/2805




"""
# target 크기보다 커지는 최대값찾기
def find_tree(list, target, left, right):
    if left > right:
        return None

    mid = (left + right) // 2

    # mid 다음부터
    if (sum(list[mid:]) - (list[mid] * (right-mid+1))) >= target:
        return find_tree(list, target, mid+1, right)
    else:
        return find_tree(list, target, left, mid-1)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

data = list(map(int, input().split()))
