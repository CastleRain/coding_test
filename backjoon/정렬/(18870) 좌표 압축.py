"""
https://www.acmicpc.net/problem/18870

자기 보다 작은 숫자가 몇개인가?

N = 100만

시간제한 2초

sort -> nlogn
700만

원래 데이터 저장 필요
정렬 ?도 해야함
index로 찾은 뒤에 값 저장
"""

import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data_sort = sorted(set(data))

data_dict = {}

for num, x in enumerate(data_sort):
    data_dict[x] = num


for d in data:
    print(data_dict[d], end = " ")
    


