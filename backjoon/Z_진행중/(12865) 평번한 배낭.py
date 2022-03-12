"""

https://www.acmicpc.net/problem/12865

N개의 물건
W무게
V가치

최대 K만큼의 무게만 넣을 수있다

물건은 하나씩만 존재한다.
조합
"""
import sys
import itertools
input = sys.stdin.readline

def solution(n, k):
    bag = []
    dp = [0] * 100001  
    for _ in range(n):
        w, v = map(int, input().split())
        bag.append([w, v])
    bag.sort() # 무게 순서대로 정리

    for i in range(1, n+1):
        check = True
        for j in itertools.combinations(bag, i):
            weight = 0
            val = 0
            for idx in range(i):
                weight += j[idx][0]
                val += j[idx][1]
                if weight > k:
                    break
                else:
                    result = max(result, val)

    return result

if __name__ == "__main__":
    n, k = map(int, input().split())

    print(solution(n ,k))

# 시간 초과
# import sys
# import itertools
# input = sys.stdin.readline

# def solution(n, k):
#     bag = []
#     result = 0
#     for _ in range(n):
#         w, v = map(int, input().split())
#         bag.append([w, v])
#     bag.sort() # 무게 순서대로 정리

#     for i in range(1, n+1):
#         check = True
#         for j in itertools.combinations(bag, i):
#             weight = 0
#             val = 0
#             for idx in range(i):
#                 weight += j[idx][0]
#                 val += j[idx][1]
#                 if weight > k:
#                     break
#                 else:
#                     result = max(result, val)

#     return result

# if __name__ == "__main__":
#     n, k = map(int, input().split())

#     print(solution(n ,k))




# 이 코드는 물건이 무한으로 있을 때 가능한 코드이다.
# import sys

# input = sys.stdin.readline

# def solution(n, k):
#     bag = []
#     dp = [0] * (k+1)
#     for _ in range(n):
#         w, v = map(int, input().split())
#         bag.append([w, v])
#     bag.sort() # 무게 순서대로 정리
#     for i in range(1, k+1):
#         for w, v in bag:
#             if i < w: # 현재 값보다 물품의 무게가 더 큰 경우는 빠져나간다.
#                 break 
#             else:
#                 if i == w:
#                     dp[i] = max(v, dp[i])
                
#                 if i - w > 0: 
#                     dp[i] = max(dp[i-w] + v, dp[i])

#     return dp[k]

# if __name__ == "__main__":
#     n, k = map(int, input().split())

#     print(solution(n ,k))




# import sys

# input = sys.stdin.readline


# def solution(n, k):
#     bag = []
#     dp = [0] * 100001

#     for _ in range(n):
#         w, v = map(int, input().split())
#         # bag.append([w, v, v/w]) # w무게, v가치, 단위당 가치
#         bag.append([w, v])
        
#     # bag.sort(key = lambda x: (x[0], -x[2])) # 단위당 가치가 큰 순서, 같다면 무게가 작은 순서대로 정리
#     bag.sort() # 무게 순서대로 정리
    
#     result = 0
#     # for w, v, _ in bag:
        
#     #     if k >= w:
#     #         result += k // w * v # 결과값에 가치만큼 더해주기
#     #         k %= w # 들수 있는 무게 없애기
        
#     #     if k == 0: # 다 채웠으면 패스
#     #         break
#     for i in range(1, k+1):
        
#         for w, v in bag:
#             if i < w: # 현재 값보다 물품의 무게가 더 큰 경우는 빠져나간다.
#                 break 
            
#             else:
#                 if i == w:
#                     dp[i] = max(v, dp[i])
                
#                 if i - w > 0: 
#                     dp[i] = max(dp[i-w] + v, dp[i])

#     return dp[k]

# if __name__ == "__main__":
#     n, k = map(int, input().split())

#     print(solution(n ,k))