"""
색종이 만들기


"""

"""
첫번째 줄은 하얀색 색종이 수 (0)
두번째 줄은 파란색 색종이 수 (1)
"""


# 내 풀이

n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))


def paper(x1, y1, x2, y2):
    