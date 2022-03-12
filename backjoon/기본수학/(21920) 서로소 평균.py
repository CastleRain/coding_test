"""
https://www.acmicpc.net/problem/21920

"""
import sys
import math
input = sys.stdin.readline

# 메모리 제한이 넉넉하니 DP로 저장
dp = [0] * 1000001


# result : X와 서로소인 값의 합
# cnt : X와 서로소인 값들의 갯수
result = 0
cnt = 0

n = int(input())
a = list(map(int, input().split()))
x = int(input())

# 배열에서 숫자를 다 가져온다.
for d in a:
    
    # 아직 서로소인지 모른다면
    if dp[d] == 0:
        
        # 비교하고 서로소라면
        if math.gcd(d, x) == 1:
            
            # dp를 1로 바꾸어주고 result와 cnt를 올려주자.
            dp[d] = 1
            result += d
            cnt += 1
        
        # 서로소가 아니라면 dp에 2를 저장해주자.
        else:
            dp[d] = 2

    # 만약 처음 들어온 숫자가 아니고 서로소라고 판별이 되었다면 바로 result와 cnt의 값을 올려주자.
    elif dp[d] == 1:

        result += d
        cnt += 1

print(result/cnt)