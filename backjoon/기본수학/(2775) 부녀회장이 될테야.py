"""
부녀회장이 될테야
"""

"""
이런순서로 올라가게된다.

2 7 16 30 55
1 3 6 10 15
1 2 3 4  5
"""

t = int(input())
data_len = 14
k, n = [], []

dp = [[0] * 14 for _ in range(data_len)]


for _ in range(t):
    k.append(int(input()))
    n.append(int(input()))

# k = 층수 , n = 호수
# 초기값 만들어놓기
for i in range(data_len):
    dp[0][i] = i+1

# 선택된 층이 2층이 아니라면 바로 밑에 호실 *2 와 이전 층의 모든 호실을 더하면된다.

#
# for kk in range(1, data_len):
#
#
#     for nn in range(data_len):
#         sum = dp[kk-1][nn]
#
#         if kk == 1:
#

"""
못품
t = int(input())

for _ in range(t):  
    floor = int(input())  # 층
    num = int(input())  # 호
    f0 = [x for x in range(1, num+1)]  # 0층 리스트
    for k in range(floor):  # 층 수 만큼 반복
        for i in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
            f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
    print(f0[-1])  # 가장 마지막 수 출력
    """
