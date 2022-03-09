"""
https://www.acmicpc.net/problem/11000

Si 시작 Ti끝 N개수업
최소 강의실 사용

Si, Ti가 같을 수 있다.
Ti <= SI 

N = 200,000

SI를 기준으로 sort진행

for 20만 -> sort() -> for 20만
"""

import sys
import heapq
input = sys.stdin.readline

def solution(n):

    data = []
    for _ in range(n):
        
        data.append(list(map(int,input().split()))) # [s, t] 형태로 저장
    
    data.sort() # data s값으로 정렬
    room = [] # 방 갯수

    # 첫번째 값 추가
    heapq.heappush(room, data[0][1])
    for i in range(1, n):
        room_end = room[0]
        if room_end <= data[i][0]: # 해당 방에 넣을 수 있다.
            heapq.heappop(room)
            heapq.heappush(room, data[i][1])
        else:# 아닌 경우 현재 값을 넣어준다.
            heapq.heappush(room, data[i][1])

    return len(room)



if __name__ == "__main__":
    n = int(input())
    print(solution(n))