"""
문제 링크 : https://www.acmicpc.net/problem/10989
푼 날짜 : 220313
문제 유형 : 정렬


풀이 : 
heapq => 메모리 초과
dict => 시간 초과 -> sys.stdin.readline추가하니까 성공..

"""



import sys
from collections import defaultdict
input = sys.stdin.readline

def solution(n):

    data = defaultdict(int)
    for _ in range(n):
        data[int(input())] += 1

    for i in sorted(data.keys()):
        for j in range(data[i]):
            print(i)
    # for _ in range(n):
    #     print(heapq.heappop(data))
    return 0

if __name__ == "__main__":
    n = int(input())
    solution(n)





# 메모리 초과
# import sys
# import heapq


# def solution(n):

#     data = []
#     for _ in range(n):
#         heapq.heappush(data, int(input()))

#     for _ in range(n):
#         print(heapq.heappop(data))
#     return 0

# if __name__ == "__main__":
#     n = int(input())
#     solution(n)