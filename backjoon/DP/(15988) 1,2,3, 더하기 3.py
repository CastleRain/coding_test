"""
https://www.acmicpc.net/problem/15988

f(n) = f(n-3) + f(n-2) + f(n-1)
"""


def solution(n):

    MAX_NUM = 1000000009
    MAX = 1000000


    dp = [0 for i in range(MAX+1)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, MAX+1):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MAX_NUM

    for _ in range(n):
        
        print(dp[int(input())])



if __name__ == "__main__":
    
    
    n = int(input())

    solution(n)
