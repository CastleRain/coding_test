"""
나무 자르기

https://www.acmicpc.net/problem/2805


min, max에서 이분 탐색을 한다.
data에서 중간값을 뺀 값이 m 값보다 작다면 min을 올리고
크다면 max값을 낮추면서 중간값을 저장한다.
끝까지 간 후 저장된 값을 출력한다.

"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

data = list(map(int, input().split()))


min_val = 0
max_val = max(data)
save_point = 0



while True:
    if min_val > max_val:
        break
    result = 0
    mid = (min_val + max_val) // 2
 
    for d in data:
        if d > mid:
            result += d-mid

    if result >= m:
        save_point = mid
        min_val = mid+1

    else:
        max_val = mid-1

print(save_point)






"""
타임아웃 걸림
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

data = list(map(int, input().split()))


min_val = 1
max_val = max(data)
save_point = 0



while True:
    if min_val > max_val:
        break
    result = 0
    mid = (min_val + max_val) // 2

    for d in data:
        if d - mid > 0:
            result += d-mid

    if result >= m:
        save_point = mid
        min_val = mid+1

    else:
        max_val = mid-1

print(save_point)
"""