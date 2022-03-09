"""
https://www.acmicpc.net/problem/20365

탐욕법

1 <= N <= 500000
R B


"""

import sys

input = sys.stdin.readline

def solution(answer):
    
    first_data = ""
    result = ""
    for ans in answer:
        if ans != first_data:
            first_data = ans
            result += first_data
    
    if result.count("B") == result.count("R"):
        return result.count("B")+1
    else:
        return max(result.count("B"), result.count("R"))



if __name__ == "__main__":
    
    input()
    answer = input()

    print(solution(answer))