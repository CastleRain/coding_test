"""
문제 링크 : https://www.acmicpc.net/problem/14863
푼 날짜 : 220324
문제 유형 : DP?




풀이 : 


"""

import sys
import itertools
input = sys.stdin.readline


def solution():

    n, m = map(int, input().split())
    data = []

    min_sum, min_val,  max_sum, max_val = 0, 0,0,0
    for _ in range(n):
        walk, walk_val, bicycle, bicycle_val = map(int, input().split())
        d = [[walk_val / walk, walk, walk_val], [bicycle_val/bicycle, bicycle, bicycle_val]]
        d.sort(key = lambda x: -x[0]) # 분당 가치가 높은 순서로 저장

        max_sum += d[0][1] # 제이 높은 가치의 분
        max_val += d[0][2] # 제일 높은 가치의 요금
        min_sum += d[1][1]
        min_val += d[1][2]
        data.append(d)
    
    if max_sum <= m:
        print(max_val)
    else:
        
        if abs(m -  min_val) > abs(m-max_val): # max_val을 기준으로 낮은 값의 배열을 하나씩 고쳐나가기
            data.sort(key = lambda x: x[0][0]) # 낮은게 처음 오게 정렬
            for i in range(1, n+1):
                for j in range()
            
        else: # min_val을 기준으로 높은 값의 배열 하나씩 고쳐나가기
            data.sort(key = lambda x: -x[0][0])  # 높은게 처음 오게 정렬






    return 0

if __name__ == "__main__":

    solution()