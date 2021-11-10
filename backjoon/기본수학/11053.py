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
            
            
            

"""



n = int(input())
data = list(map(int, input().split()))

# 4번째 풀이
dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1


for i in range(n-1, -1, -1):



    for j in range(i-1, -1, -1):

        max_num = 0

        if data[i] > data[j]:

            max_num += dp[i][i]+1

            dp[j][i] = max_num


    dp[i][i] = max(dp[i])
print(dp)
# 2번째 풀이
# dp = [[0] * n for _ in range(n)]
# dp2 = [[0] * n for _ in range(n)]
#
# for i, d in enumerate(data):
#
#     val = data[i]
#
#
#     for j in range(i+1, n):
#
#         compare_val = data[j]
#
#         # 현재 값보다 큰경우 1로 초기화한다.
#         if val < compare_val:
#
#             # 만약 비교했는데 1인경우에 윗행역시 1이면 그대로 뒷 값을 가져온다.
#             if i-1 >= 0 and dp[i-1][j] == 1:
#                 dp[i][j:] = dp[i-1][j:]
#
#                 # 이전값을 가져오고 다음 행으로 넘어간다.
#                 break
#
#             else:
#
#                 dp[i][j] = 1
#
#                 # 현재값을 비교하는 값으로 바꾼다.
#                 val = compare_val
#
#
#
#         # 첫번쨰 풀이에 들어간 내용
#         # val = data[i]
#         # compare_val = data[j]
#         #
#         # if val < compare_val:
#         #     max+=1
#         #     val = compare_val
#
#
#
#         # # 현재 값보다 큰경우 1로 초기화한다.
#         # if val < compare_val:
#         #
#         #     # 만약 비교했는데 1인경우에 윗행역시 1이면 그대로 뒷 값을 가져온다.
#         #     if i-1 >= 0 and dp[i-1][j] == 1:
#         #         dp[i][j:] = dp[i-1][j:]
#         #
#         #         # 이전값을 가져오고 다음 행으로 넘어간다.
#         #         break
#         #
#         #     else:
#         #
#         #         dp[i][j] = 1
#         #
#         #         # 현재값을 비교하는 값으로 바꾼다.
#         #         val = compare_val
#
# print(dp)




