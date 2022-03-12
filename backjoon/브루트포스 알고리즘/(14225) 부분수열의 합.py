"""
https://www.acmicpc.net/problem/14225


sort -> 2개 합이 그 다음 숫자보다 작다면 그 사이의 작은 숫자가 답이다.

아무리커도 2,000,000 보단 작다.

하나씩 키워가며 더해간다.

"""

from itertools import combinations

dp =  [0]*2000001
dp[0] = 1

n = int(input())
data =  list(map(int, input().split()))

for i in range(1, n+1): # n번 돌면서   
    for j in combinations(data, i): # i개 뽑아내는 조합을 가져온다.
        dp[sum(j)] = 1
    
print(dp.index(0))










# from itertools import combinations


# dp =  [0]*2000001
# dp[0] = 1

# n = int(input())
# data =  list(map(int, input().split()))
# for d in data:
#     dp[d] = 1
# check = True
# # 돌면서 
# min_sum = 1# min_sum : 지금까지 더해진 제일 작은 수 1부터 시작해야하므로 1부터 저장
# for i in range(2, n+1): # n번 돌면서
#     max_sum = 0 
    
#     for j in combinations(data, i): # i개 뽑아내는 조합을 가져온다.
#         sum_result = sum(j)
#         max_sum = max(max_sum, sum_result)

#         dp[sum_result] = 1
    
#     try: # 0이 있는지 판단
#         print(min_sum + dp[min_sum:max_sum+1].index(0))
#         check = False
#         break

#     except: # 0이 없으므로 다음으로 넘어가면된다.
#         min_sum = max_sum
#         continue
        
# if check:
#     print(dp.index(0))