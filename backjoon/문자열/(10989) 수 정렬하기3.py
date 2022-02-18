"""
https://www.acmicpc.net/problem/10989

"""
from collections import defaultdict
import sys
input = sys.stdin.readline
n = int(input())

num_dic = defaultdict(int)

for _ in range(n):
    num = int(input())
    num_dic[str(num)] += 1


# num_dic_sort = sorted(num_dic, key = lambda x : x[0])


for i in sorted(list(num_dic.keys())):
    for _ in range(num_dic[str(i)]):
        print(int(i))
