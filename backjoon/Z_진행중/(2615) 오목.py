"""
https://www.acmicpc.net/problem/2615

19 * 19

검은 바둑알 : 1
흰 바둑알 : 2

승리한 바둑알이 없으면 0
검은 1
흰 바둑 2

이긴 경우가 발생하면 왼쪽 가장 위쪽에 있는 좌표를 출력

숫자가 들어오면 오른쪽으로 검색, -> 현재값이 정답
오른쪽 대각선 검색, -> 현재 값이 정답
아래로 검색 -> 현재 값이 정답
왼쪽 대각선으로 검색 -> 만약 된다면 마지막의 숫자가 결과
"""

import sys

input = sys.stdin.readline

data = []
for _ in range(19):
    data.append(list(map(int, input().split())))

def check(color, x, y):
    # 변경 순서 : 오른쪽, 오른쪽 대각선, 아래, 왼쪽 대각선
    dir_x = [0, 1, 1, 1]
    dir_y = [1, 1, 0, -1]

    for i in range(4):
        for 


for i in range(19):
    for j in range(19):
        # 검은 바둑 돌
        if data[i][j] == 1:

            print(data[i][j])

