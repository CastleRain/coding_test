"""
https://www.acmicpc.net/problem/1620

"""

import sys

input = sys.stdin.readline

n, m  = map(int, input().split())

data = []
data_num = {}

for i in range(n):
    name = input().rstrip()
    data.append(name)
    data_num[name] = i+1

for _ in range(m):
    
    text = input().rstrip()

    if text.isalpha():
        print(data_num[text])
    else:
        print(data[int(text)-1])


# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())

# data = []
# for _ in range(n):
#     data.append(input().rstrip())


# for _ in range(m):
    
#     text = input().rstrip()

#     if text.isalpha():
#         print(data.index(text)+1)
#     else:
#         print(data[int(text)-1])