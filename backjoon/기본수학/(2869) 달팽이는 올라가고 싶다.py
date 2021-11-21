"""
달팽이는 올라가고 싶다


"""

# 낮 : A 밤 : B 나무막대 : V
import math
a, b, v = map(int, input().split())

real_v = v - a

count = 1 + math.ceil(real_v / (a-b))

print(int(count))
