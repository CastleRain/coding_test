"""
https://www.acmicpc.net/problem/16918

R*C
0=> 폭탄 나둠
1 => 아무것도 안함
2 => 나머지 다 폭탄으로 채움
3 => 0이 터짐
4 => 나머지 다 채움
5 => 2가 터짐 == 1 
6 -> 나머지 다 채움 == 2
7 -> 0이 터짐 == 3
8 == 4

"""

import sys

input = sys.stdin.readline


def solution(data, n):
    # 상 우 하 좌
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    n %= 4
    if n == 1:
        return data
    elif n==2:
        r = len(data)
        c = len(data[0])
        data = []
        for _ in range(r):
            data.append("O"*c)
        return data
    elif n == 3:
        r = len(data)
        c = len(data[0])
        data_result = [["O"] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if data[i][j] =="O":
                    data_result[i][j] = "."
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if nx <= r-1 and nx >= 0 and ny <= c-1 and ny >= 0:
                            data_result[nx][ny] = "."
        data = []
        for i in range(r):
            data.append("".join(data_result[i]))

        return data 
    else:
        r = len(data)
        c = len(data[0])
        data = []
        for _ in range(r):
            data.append("O"*c)
        return data

if __name__ == "__main__":
    r, c, n = map(int, input().split())
    data = []
    for _ in range(r):
        data.append(input().strip())

    result = solution(data, n)
    for i in range(r):
        
        print(result[i])