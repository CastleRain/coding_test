"""
분수찾기
https://www.acmicpc.net/problem/1193

시간제한 0.5초
"""


# def find_num(num):
#     return int(1 + (num ** 2 - num) / 2)
#
#
# n = int(input())
# count = 1
# while True:
#     if n<find_num(count):
#         break
#     count+=1
#
# a = count - (n - find_num(count-1) + 1)
# b = count - a
#
#
# print(f"{b}/{a}")



x = int(input())
num_list = []

num = 0
num_count = 0

while num_count < x:
    num += 1
    num_count += num

num_count -= num

if num % 2 == 0:
    i = x - num_count
    j = num - i + 1
else:
    i = num - (x - num_count) + 1
    j = x - num_count

print(f"{i}/{j}")
