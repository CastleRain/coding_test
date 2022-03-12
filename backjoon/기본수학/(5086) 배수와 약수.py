"""
배수와 약수
https://www.acmicpc.net/problem/5086

"""

import sys

input = sys.stdin.readline


while True:

    n, m = map(int, input().split())

    # n, m이 0이면 break
    if n == 0 and m == 0:
        break

    if n > m:
        if n % m == 0:
            print("multiple")
        else:
            print("neither")
    else:
        if m % n == 0:
            print("factor")
        else:
            print("neither")
