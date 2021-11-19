"""
가장 긴 증가하는 부분 수열

"""

"""
첫번째 풀이
    1. 행렬로 만들어서 풀기
    -> n만큼의 행렬을 생성
    -> for k in range(n)
        for m range(k+1,n)
    -> 돌면서 큰 수열이 나오면 1로 넣어주기
    -> 만약 비교한 값의 결과가 1이고 윗 행이 존재하고 같은 열의 값이 1인경우 뒷 값 가져오기
    -> 최대 O(n^2/2) 최소 O(n)
    -> 시간 충분할것으로 생각
    
    -----> [1 1000 30 20 21 22 23] 의경우 안됨 a에서 계속 돌면서도 봐야함1 
    
두번째 풀이
    1. 첫번쨰 풀이와 비슷하게 진행
    2. 0,1이 아닌 합계 저장할 예정

세번째 풀이 : 링크드리스트 생각중
    1. 받아온 리스트 뒤에서부터 진행
        ex) a b c d e f // o인경우 증가하는 수열 성립 x인경우 감소
            e -> f (o)
            
            d -> e (x)
            d -> f (o)
            
            c -> d (o) (이경우 d에서 가장 긴 수열 받아오기)
            c- > d -> f(o)
            c -> f (o)
            
            b -> c (o) (이경우 c에서 가장 긴 수열 받아오기)
            b -> c -> d -> f
            
            a -> b (x)
            a -> c (o) (이경우 c에서 가장 긴 수열 받아오기)
            a -> c -> d -> f
            
4번째 풀이 : 뒷 행렬부터 시작해서 최장 길이값을 저장해서 가져오자. 이후 최대값 출력을 진행한다.

완벽한 풀이 (인터넷참고) : 

이 문제의 풀이법은 총 2가지가 있다. 
    1. dp
    2. 이분 탐색
    
나는 2가지중 dp만 이용했으며 2차원으로 진행했으므로 1차원으로 진행한 풀이보다 더 공간 차지가 많다.(실제로 골드문제로만 올라가도 메모리부족이 뜬다.)

            

"""

# 인터넷 풀이

# x = int(input())
#
# arr = list(map(int, input().split()))
#
# dp = [1 for i in range(x)]
#
# for i in range(x):
#     for j in range(i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i], dp[j]+1)
#             print(f"j = {j}")
#             print(f"i = {i}")
#             print(dp)
#
# print(max(dp))

import bisect

x = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]

for i in range(x):

    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        print(f"idx = {idx}")
        dp[idx] = arr[i]
    print(f"i = {i}")
    print(f"arr = {arr}")
    print(f"dp = {dp}")
    print("--------------")

print(len(dp))


# 4번째 풀이
# n = int(input())
# data = list(map(int, input().split()))
#
# # 4번째 풀이
# dp = [[0] * n for _ in range(n)]
#
# for i in range(n):
#     dp[i][i] = 1
#
#
# """
# ## 5,5 -> 4,5 -> 4,4 -> 3,5 -> 3,4 -> 3,3
# for a in range(n-1, -1, -1):
#     for b in range(n-1, a-1, -1):
#         print(f"{a},{b}")
#
# """
# max_result = 0
# for i in range(n-1, -1, -1):
#
#     for j in range(n-1, i-1, -1):
#
#         max_num = 0
#
#         if data[i] < data[j]:
#
#             max_num += dp[j][j]+1
#
#             dp[i][j] = max_num
#
#
#     dp[i][i] = max(dp[i])
#     max_result = max(max_result, max(dp[i]))
#
#
# print(max_result)
#
# # 2번째 풀이
# # dp = [[0] * n for _ in range(n)]
# # dp2 = [[0] * n for _ in range(n)]
# #
# # for i, d in enumerate(data):
# #
# #     val = data[i]
# #
# #
# #     for j in range(i+1, n):
# #
# #         compare_val = data[j]
# #
# #         # 현재 값보다 큰경우 1로 초기화한다.
# #         if val < compare_val:
# #
# #             # 만약 비교했는데 1인경우에 윗행역시 1이면 그대로 뒷 값을 가져온다.
# #             if i-1 >= 0 and dp[i-1][j] == 1:
# #                 dp[i][j:] = dp[i-1][j:]
# #
# #                 # 이전값을 가져오고 다음 행으로 넘어간다.
# #                 break
# #
# #             else:
# #
# #                 dp[i][j] = 1
# #
# #                 # 현재값을 비교하는 값으로 바꾼다.
# #                 val = compare_val
# #
# #
# #
# #         # 첫번쨰 풀이에 들어간 내용
# #         # val = data[i]
# #         # compare_val = data[j]
# #         #
# #         # if val < compare_val:
# #         #     max+=1
# #         #     val = compare_val
# #
# #
# #
# #         # # 현재 값보다 큰경우 1로 초기화한다.
# #         # if val < compare_val:
# #         #
# #         #     # 만약 비교했는데 1인경우에 윗행역시 1이면 그대로 뒷 값을 가져온다.
# #         #     if i-1 >= 0 and dp[i-1][j] == 1:
# #         #         dp[i][j:] = dp[i-1][j:]
# #         #
# #         #         # 이전값을 가져오고 다음 행으로 넘어간다.
# #         #         break
# #         #
# #         #     else:
# #         #
# #         #         dp[i][j] = 1
# #         #
# #         #         # 현재값을 비교하는 값으로 바꾼다.
# #         #         val = compare_val
# #
# # print(dp)
#



