"""
https://www.acmicpc.net/problem/2141

N <= 10만
X <= 10억
A <= 10억

0
1 A[i]명
2 A[2]명...
3
4
5
6

전체다 만들수는 없다. 누적합해서 /2의 위치가 어디인지 파악하자. -> 탐색은 이분탐색?
위치파악되면 해당 값이 
 |X[i]| ≤ 1,000,000,000, -> 음수로도 간다는건가?
1 0 0 0 1
    x 

0 1 2 3
  3 5 3
  3*1   3*1  
"""

import sys

input = sys.stdin.readline


def solution(n, data):
    

    # 이분탐색

    
    for i in range(n, -1, -1):
        if i == n:



    return 0

if __name__ == "__main__":
    n = int(input())

    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))

    data.sort()

    solution(n, data)