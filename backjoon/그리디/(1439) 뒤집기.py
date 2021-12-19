"""
뒤집기
https://www.acmicpc.net/problem/1439

공간복잡도가 늘어날 수 있지만 생각한 방법은
input으로 받아온 데이터 n을 for문으로 돌면서 이전값과 같은 값인지 확인 -> 같은 값이면 패스 다른값이면 데이터 저장
counter를 이용하여 최솟값 출력

예를 들어 abbbba가 있다고치자.
이 경우 bbbb가 변환될때 한번에 변환되므로 b라고 봐도 무방하다.
aba라고하게되면 b하나만 변환하면 다 같은값이 되는것을 확인할 수 있으므로 최솟값을 알 수 있다.

s의 길이가 100만보다 적다고 했지만 input으로 한번에 많은값을 받으면 시간이 걸릴수 있으므로 sys.stdin.readline을 사용하여 시간 절약을 하자.

-> 두가지 경우를 제외못했다.
1. 하나도 안들어온경우
2. 하나의 숫자로만 구성된경우

"""

import collections
import sys

input = sys.stdin.readline

s = input().rstrip()
count = collections.Counter()

data = []

# 첫번째 값은 추가.
if len(s) == 0:
    print(0)
else:
    data.append(s[0])

    for s_data in s[1:]:

        # 만약 데이터의 마지막값과 다른값이 들어오면 데이터에 추가해주자
        if data[-1] != s_data:
            data.append(s_data)

    count.update(data)
    if len(count) == 1:
        print(0)
    else:
        print(min(count.values()))