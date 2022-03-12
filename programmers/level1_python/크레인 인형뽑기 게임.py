"""
https://programmers.co.kr/learn/courses/30/lessons/64061
22.02.21

각 열별로 list를 저장해놓고 list pop을 진행해주면 될것이다.



"""
from collections import deque

def solution(board, moves):
    answer = 0

    crain = []

    # deque의 범위만큼 저장
    for _ in range(len(board)):
        crain.append(deque([]))
    
    for board_line in board:
        for num, b in enumerate(board_line):
            # 만약 인형이 들어온다면
            if b != 0:
                crain[num].appendleft(b)

    result = []

    for m in moves:
        # 비어있는 칸이 아니라면
        if len(crain[m-1]) != 0:
            now_num = crain[m-1].pop()
            if len(result) != 0:
                if result[-1] == now_num:
                    result.pop()
                    answer += 2
                else:
                    result.append(now_num)
            else:
                result.append(now_num)

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))