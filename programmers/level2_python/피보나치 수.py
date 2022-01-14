"""
dp 이용해야한다 -> dp를 이용하면 시간초과 걸림
만약 dp가 존재한다면 
"""
# def fibo(dp, x):
#     # 0 패스
#     if dp[x] != -1:
#         return dp[x]
#     else:
#         dp[x] = fibo(dp, x-1) + fibo(dp, x-2)
#         return dp[x]
    
    

# def solution(n):
#     # 100,000개까지 들어올 수있으므로
#     dp = [-1] * 100000
#     dp[0] = 0
#     dp[1] = 1
#     dp[2] = 1
#     return fibo(dp, n) % 1234567

def solution(n):
    li = [0,1]
    for i in range(2,n+1):
        li.append(li[i-1] + li[i-2])
    return li[-1] %1234567

if __name__ == "__main__":
    
    n = 3

    # 2
    
    print(solution(n))