"""
bfs로 풀기엔 저장하는게 너무 어렵다

백트로 풀면 시간 제한에 안걸릴려나?

그래도 백트로 풀어야할듯?

"""

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

# 데이터 n-1까지 만들어 놓기
data = [0] * (n-1)

# 점프 못하는 돌은 -1로
for _ in range(m):
    data[int(input())] = - 1

min_val = 1e9
def jump(dir, val, speed):
    global min_val

    if dir+speed > n-2:
        return

    elif dir+speed == n-2:
        min_val = min(min_val, val)
        return

    elif data[dir+speed] != -1: # 지나지 못하는 돌이 아닌 경우
        if dir == 1:
            jump(2,1,1)
        
        elif speed == 1: # 1 or 2로 줄수 밖에 없다.
            jump(dir+2, val+1, 2)
            jump(dir+1, val+1, 1)
        else:
            jump(dir+speed+1, val+1, speed+1)
            jump(dir+speed-1, val+1, speed-1)
    else:
        return

jump(1, 0, 1)

if min_val == 1e9:
    print(-1)
else:
    print(min_val)
        





# import sys
# from collections import deque
# input = sys.stdin.readline

# n, m = map(int, input().split())

# # 데이터 n-1까지 만들어 놓기
# data = [0] * (n-1)

# # 점프 못하는 돌은 -1로
# for _ in range(m):
#     data[int(input())] = - 1

# # 처음은 무조건 1
# data[2] = (1, 1, 1) # 1만에 왔고 1의 가속도를 가지고 있으며, 총 n번 진행했다.

# # 그 다음부터는 가속도 가능
# queue = deque(data[2])


# while queue:

#     val, speed, cnt = queue.popleft()
#     if val == n-2:

#     if speed == 1: # 줄일 수 없다.
#         queue.append((val+1, 1, cnt + 1))
#         queue.append((val+2, 2, cnt + 1))
#     else:
#         queue.append((val + speed -1 , speed - 1))
#         queue.append((val + speed + 1, speed + 1))
