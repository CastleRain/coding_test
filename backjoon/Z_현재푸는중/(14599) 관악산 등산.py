"""
문제 링크 : https://www.acmicpc.net/problem/14699
푼 날짜 : 220323
문제 유형 : dp, 그래프


풀이 : 

높은것부터 정렬 후 dfs진행

dfs 끝까지 가지면 값 리턴

dfs해서 만약 자기 보다 높은 값에 값이 들어가있으면 해당 값 가져오기 (DP)



"""

import sys



def solution():
    n, m = map(int, input().split())
    dp = [[1] for _ in range(n+1)] # 자기자신도 간것으로 치기 때문에 1로 초기화
    data = []

    graph = [[] for _ in range(n+1)]

    for i, num in enumerate(list(map(int, input().split()))):
        data.append([i+1, num])
        

    
    for _ in range(m):
        a, b = map(int, input().split())
        if data[a-1][1] > data[b-1][1]:
            graph[b].append(a)
        else:
            graph[a].append(b)
    data.sort(key = lambda x: -x[1])

    for i in range(len(data)):
        if len(graph[data[i][0]]) == 0:
            continue

        for v in graph[data[i][0]]:
            max_val = max(dp[data[i][0]], )



    return 0

if __name__ == "__main__":

    solution()







# import sys
# import heapq


# def dfs(depth, index, visited):

#     max_num = 0
#     visited[index] = True

#     for i in graph[index]:
#         if not visited[i] and data_save[index] < data_save[i]: # 방문하지 않았고 자기보다 높은곳에 위치한 곳인 경우
#             if dp[i] != 1: # 이미 다른곳에서 최대값까지 비교가 끝이났다.
#                 max_num = max(max_num, dp[i] + dp[index])
#             else: # 아직 비교가 되지 않았다.
#                 dfs(data_save[i-1], i, visited)



#     return 0



# def solution(data):

#     while data:
#         visited = [[False] for _ in range(n+1)]
#         num, i = heapq.heappop(data)
#         dfs(-num, i, visited)



#     return 0

# if __name__ == "__main__":
    

#     n, m = map(int, input().split())
#     dp = [[1] for _ in range(n+1)] # 자기자신도 간것으로 치기 때문에 1로 초기화
#     data, data_save = [], []

#     graph = [[] for _ in range(n+1)]

#     for i, num in enumerate(list(map(int, input().split()))):
#         data_save.append(num)
#         heapq.heappush(data, (-num, i+1)) # 현재 높이, index번호 순서대로 저장

    
#     for _ in range(m):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#         graph[b].append(a)

#     solution(data)