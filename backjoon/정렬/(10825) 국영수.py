"""
https://www.acmicpc.net/problem/10825

국어 점수가 감소하는 순서로
국어 점수가 같으면 영어 점수가 증가하는 순서로
국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)

일단 국어점수를 기준으로 정렬을 진행한다.

"""
import sys
input = sys.stdin.readline
n = int(input())

data = []
for _ in range(n):
    name, korean, english, math = input().split()
    data.append((name, int(korean), int(english), int(math)))



for i in sorted(data, key = lambda x : (-x[1], x[2], -x[3], x[0])):
    print(i[0])
