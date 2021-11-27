"""
https://www.acmicpc.net/problem/18352

인접 행렬로 구하여 그 행렬의 [x][y] 에서 y가 변함에 따라 k가 나오는 갯수를 리턴해주면된다.
-> N이 너무커서 인접 리스트로 구현해야할것같다.

"""

n, m, k, x = map(int, input().split())

for _ in range(m):
