n = int(input())
array = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_val = -1e9
min_val = 1e9

def dfs(i, now):
    """
    i: array의 index(1번째부터 시작)
    now: 연산 수행한 실시간 결과값
    """
    global max_val, min_val, add, sub, mul, div
    if i == n:
        max_val = max(now, max_val)
        min_val = min(now, min_val)
    else:
        # 더하기
        if add > 0:
            add -= 1
            dfs(i + 1, now + array[i])
            add += 1   # 다른 경우의 수도 탐색해야 하므로 add 연산횟수 원상복구
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - array[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * array[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / array[i]))  # now // array[i] 하면 에러 발생함..
            div += 1


dfs(1, array[0])
print(max_val)
print(min_val)