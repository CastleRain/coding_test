"""
문제 링크 : https://www.acmicpc.net/contest/problem/770/1
푼 날짜 : 220312
문제 유형 : 백트래킹?


풀이 : 


"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline



def solution(a, b, c, result):
    global cnt
    if [a,b,c].count(0) == 2:
        cnt = max(cnt, result)
        exit(0)
        return
    # 2개가 1인 경우
    elif [a,b,c].count(0) == 1:
        if a ==0:
            solution(a+1, b-1, c-1, result+1)
        elif b == 0:
            solution(a-1, b+1, c-1, result+1)
        else:
            solution(a-1, b-1, c+1, result+1)
    # 3개가 1인 경우
    else:
        solution(a-1, b-1, c+1, result+1)
        solution(a-1, b+1, c-1, result+1)
        solution(a+1, b-1, c-1, result+1)

if __name__ == "__main__":
    
    n = int(input())
    for i in range(n):
        cnt = 0
        a, b, c = map(int, input().split())
        solution(a, b, c, 0)
        if cnt % 2 == 0:
            print("R")
        else:
            print("B")