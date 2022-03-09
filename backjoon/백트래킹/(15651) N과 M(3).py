"""
https://www.acmicpc.net/problem/15651
중복허용이다.

visited가 의미없다.


"""


import sys

input = sys.stdin.readline

n, m = map(int, input().split())
result = []


def n_m(result):

    if len(result) == m:

        print(" ".join(result))
        return

    
    for i in range(n):

        result.append(str(i+1))
        n_m(result)
        
        result.pop()

n_m(result)
