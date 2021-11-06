"""
ACM 호텔
"""

"""
풀이방법
H : 층수 W : 방수  N : 몇번방

엘리베이터 움직이는 수는 고려안하므로
ceil(N/H) -> 고려되는 방
N%H -> 0인경우 옥상층
"""

import math

c = int(input())

data = []
for _ in range(c):
    data.append(list(map(int, input().split())))

for h, w, n in data:

    if n%h == 0:
        floor = h
    else:
        floor = n%h
    room = str(math.ceil(n/h)).zfill(2)
    print(f"{floor}{room}")