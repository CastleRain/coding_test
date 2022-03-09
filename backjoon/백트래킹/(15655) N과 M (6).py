"""
https://www.acmicpc.net/problem/15655

"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
for i in list(map(int, input().split())):
    data.append(i)
result = []
data.sort()
visited = [False] * n

def n_m(first, result,visited):

    if len(result) == m:
        print(" ".join((result)))
        return

    
    for i in range(first, n):
        
        if not visited[i]:
            
            visited[i] = True
            result.append(str(data[i]))

            n_m(i, result,visited)

            a = result.pop()
            visited[data.index(int(a))] = False

n_m(0, result, visited)