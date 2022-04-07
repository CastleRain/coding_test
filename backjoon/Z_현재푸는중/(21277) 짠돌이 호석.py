"""
문제 링크 : https://www.acmicpc.net/problem/21277
푼 날짜 : 220321
문제 유형 : 구현


풀이 : 

두개의 퍼즐 N1, M1  / N2, M2

액자의 가격 : 액자의 넓이에 결정된다.
각 퍼즐은 90 180 270도 회전이 가능하다.

하나는 그대로 나두고 나머지 하나를 4번 돌리면서 넣어본다.

graph = 150*150 으로 다 0이 들어가게 하자.

n, m이 50 이하이므로 첫번째 값을 50,50에서부터 시작해서 넣어주고

두번째 값을 모든 1의 값을 하나씩 다 n,m안의 값안에 하나씩 대입해보자.

-> 대입을 할 때 마다 최소 넓이를 구하는 함수를 만들어주자. (1을 받은 왼쪽위, 오른쪽 위 왼쪽 아래 오른쪽 아래)
=> i, j (i=행 j= 열)이라 할 때 i의 최소값 i의 최대값, j의 최솟값, j의 최댓값을 기록한다. 이후 사각형을 

=> 150 * 150 = 약 만번
=> 2번째 그래프에서 1의 갯수만큼 위의 값을 실행 최대 2500   O(2500) => 중간에 못들어가는 값이 있다면 바로 나갈 수 있으므로 이것보단 짧다.
-> 4방향으로 보아야하므로 *4
=> 최악의 경우 1억 넘지만 시간 제한 2초이므로 가능할 거 같다.

"""

import sys


MAX_NUM = 151

# 넓이 
def graph_area(graph, min_area):

    x1, y1, x2, y2 = 1e9, 1e9, -1, -1

    for i in range(MAX_NUM):
        for j in range(MAX_NUM):
            if graph[i][j] == 1:
                x1, y1 = min(x1, i), min(y1, j)
                x2, y2 = max(x2, i), max(y2, j)

    now_area = (y2-y1+1) * (x2 - x1+1)

    return min(min_area, now_area)

def graph_rotate(graph, dir):
    row = len(graph)
    col = len(graph[0])

    # 0 : 90도 회젼 
    if dir == 0:
        graph_rot = [[] * row for _ in range(col)]

        for i in range(col):
            for j in range(row):
                graph_rot[i][j] = graph[j][i]
        return graph_rot

    # 1 : 180도 회전
    elif dir == 1:



    # 2 : 270도 회전


    


def solution():

    area = 1e9
    # 150 150 행렬
    graph = [[0] * MAX_NUM for _ in range(MAX_NUM)]

    for i in range(2):
        if i == 0: # 첫번째 값은 graph에 바로 입력
            n, m = map(int, input().split())
            data = []
            for _ in range(n):
                data.append(list(map(int, input())))

            for a in range(n):
                for b in range(m):
                    graph[a+50][b+50] = data[a][b]
        
        # 두번째 데이터 저장
        else:
            n2, m2 = map(int, input().split())
            data = []
            for _ in range(n2):
                data.append(list(map(int, input())))

    # 4방향
    for _ in range(4):



    return graph_area(graph, 1e9)

if __name__ == "__main__":

    print(solution())