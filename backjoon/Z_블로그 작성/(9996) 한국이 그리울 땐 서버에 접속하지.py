"""
문제 링크 :  https://www.acmicpc.net/problem/9996
푼 날짜 : 220311
문제 유형 : 문자열, 완전탐색


풀이 : 
특정 패턴과 일치하는 파일 이름을 적절히 출력하지 못한다.

n이 작으니까... 그냥 다 돌면서 확인하면 될듯?


처음과 끝은 *이 아니다.

중간은 어떻게 될지 모른다?

abc*c

=> abc -> x가 나와야함

데이터비교후 안빼면 답 안나옴

"""

import sys

input = sys.stdin.readline


def solution(n):
    yes, no = "DA", "NE"
    first, second = map(str, input().strip().split("*"))

    for _ in range(n):
        
        d = input().strip()
        
        if first == d[:len(first)]: # 처음 값과 같은지 확인
            d = d[len(first):] # 같다면 해당 값은 없애기
        else:
            print(no)
            continue # 만약 답이 아니면 다음 문자 확인

        if second == d[-len(second):]: # 두번째 값 같은지 확인
            print(yes)
        else:
            print(no)
    return 0

if __name__ == "__main__":
    n = int(input())
    solution(n)