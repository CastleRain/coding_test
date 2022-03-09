"""
https://www.acmicpc.net/problem/2667

1. DFS vs BFS
2. 인접행렬 vs 인접리스트

dfs로 진행


"""

n = int(input())

data = []

# 데이터 만들기
for i in range(n):
    data.append(list(map(int, input())))

data_sum = sum([sum(d) for d in data])

def dfs(x, y):
    global num
    if x <= -1 or x >= n or y<= -1 or y>= n:
        return False
    
    if data[x][y] == 1:
        data[x][y] = 0
        num += 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False
result = 0
result_list = []

for i in range(n):
    for j in range(n):
        num = 0
        if dfs(i,j):
            result_list.append(num)
            result += 1

print(result)
result_list.sort()
for i in result_list:
    print(i)
