"""
https://www.acmicpc.net/problem/11659

"""
import sys
input = sys.stdin.readline


n, m  = map(int, input().split())

sum_data = [0 for i in range(n+1)]

for num, d in enumerate(list(map(int, input().split()))):
    sum_data[num+1] = sum_data[num] + d

for _ in range(m):
    i, j = map(int, input().split())
    print(sum_data[j] - sum_data[i-1])