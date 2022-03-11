"""
https://www.acmicpc.net/problem/10844


"""

import sys

input = sys.stdin.readline

MAX_NUM = 1000000000 

def solution(n):
    dp = [0] * (n+1)
    dp[1] = 9
    for i in range(2, n+1):
        if i % 2 == 0:
            dp[i] = (dp[i-1] * 2 - 1)
        else:
            dp[i] =( dp[i-1] * 2)

    return dp[n]% MAX_NUM

if __name__ == "__main__":
    n = int(input())
    print(solution(n))