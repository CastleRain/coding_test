"""
숫자 카드2


"""
from collections import defaultdict
import sys
data = defaultdict(int)

input()

for i in sys.stdin.readline().split():
    data[i] += 1
input()

for j in sys.stdin.readline().split():
    print(data[j], end=" ")