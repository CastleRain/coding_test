"""
https://programmers.co.kr/learn/courses/30/lessons/12899

3진수로 만든 후 
0->1
1->2
2->4
로만 바꾸면되는것

"""

from collections import deque

n = int(input())

result = deque()




while n != 0:
    a = n % 3
    n //= 3

    result.appendleft(a)

solu = []

for i in result:
    if i == 0:
        solu.append("1")
    elif i == 1:
        solu.append("2")
    else:
        solu.append("4")

print("".join(solu))