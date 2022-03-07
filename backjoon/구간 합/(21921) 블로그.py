"""
https://www.acmicpc.net/problem/21921


누적합으로 계속 저장 

n일이 주어지고 x일동안 얼마나 들어오는가
data_sum(n-1) + data(n) - data(n-3)

"""
import sys

input = sys.stdin.readline
n, x = map(int, input().split())
data_sum = [0 for i in range(n+1)]

data = list(map(int, input().split()))

for i in range(n):
    data_sum[i+1] = data_sum[i] + data[i]
data_result = data_sum.copy()
for j in range(x, n+1):
    data_result[j] -= data_sum[j-x]
max_data = max(data_result)
max_cnt = data_result.count(max_data)


if max_data == 0:
    print("SAD")
else:
    print(max_data)
    print(max_cnt)