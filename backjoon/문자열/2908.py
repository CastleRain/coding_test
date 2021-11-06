"""
상수

https://www.acmicpc.net/problem/2908


"""

n, m = map(str, input().split())

n = int(n[2] + n[1] + n[0])
m = int(m[2] + m[1] + m[0])

print(max(n, m))