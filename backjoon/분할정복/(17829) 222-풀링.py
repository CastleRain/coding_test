"""
https://www.acmicpc.net/problem/17829


x_s, x_e, y_s, y_e를 각각 받아서 진행

진행되면서 점점 줄게되고 마지막 result[0][0]을 출력시켜주면된다.
"""

import sys

input = sys.stdin.readline


def solution(x_s, x_e, y_s, y_e):
    global result
    if x_e - x_s == 2: # 2,2만 남은 경우 (4개의 사각형만 남았으므로 정리를 진행해야한다.)
        data = []
        for x_idx in range(x_s, x_e):
            for y_idx in range(y_s, y_e):
                data.append(result[x_idx][y_idx])
        data.sort(reverse=True)
        result[x_s//2][y_s//2] = data[1]
    else:
        solution(x_s, (x_s+x_e)//2, y_s, (y_s+y_e)//2)
        solution(x_s,  (x_s+x_e)//2, (y_s+y_e)//2, y_e)
        solution( (x_s+x_e)//2, x_e, y_s, (y_s+y_e)//2)
        solution( (x_s+x_e)//2, x_e, (y_s+y_e)//2, y_e)
    

if __name__ == "__main__":
    n = int(input())
    result = []
    for _ in range(n):
        result.append(list(map(int, input().split())))

    while n != 1:
        solution(0,n,0,n)
        n//=2
    print(result[0][0])