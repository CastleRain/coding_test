"""
https://www.acmicpc.net/problem/15652

중복허용
자기 자신을 받아오긴하나 자기보다 낮은숫자는 받아오면 안된다.


"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
result = []

def n_m(last_num, result):

    if len(result) == m:

        print(" ".join(result))
        return

    
    for i in range(last_num, n):

        result.append(str(i+1))

        n_m(i, result)

        result.pop()

n_m(0, result)