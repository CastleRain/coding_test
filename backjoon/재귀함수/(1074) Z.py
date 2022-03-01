"""
https://www.acmicpc.net/problem/1074

하나씩 계산해서 가면 시간 초과에 걸리지 않을까?

1. r,c가 2^n * 2^n의 몇 번째 n에 속하는지 먼저 판단하자.
2. 1,2,3,4사분면으로 나누듯이 어디에 속하는지 판단하고 계산하면 끝일듯?

1 <= n <= 15
0 <= r, c <= 2^n

1. 해당 행열이 몇번째 사분면위인지
2. 다시 리턴
"""


# find_q : 해당 숫자가 몇사분면 위인지 확인 하고 
# n : 어느정도 크기의 배열인지
# r : r행
# c : c열

def find_num(n, r, c):

    if n == 1: # 제일 작은 사각형까지 온 경우
        
        return find_q(n, r, c)
    
    # 몇사분면인지 확인
    result = find_q(n, r, c)
    if result == 0: # 1사분면인 경우

        return find_num(n-1, r, c)
    
    elif result == 1: # 2사분면인 경우

        return 2**(2*(n-1))*1 + find_num(n-1, r, c-2**(n-1))

    elif result == 2: # 3사분면인 경우

        return 2**(2*(n-1))*2 + find_num(n-1, r-2**(n-1), c)

    else: # 4사분면인 경우

        return 2**(2*(n-1))*3 + find_num(n-1, r-2**(n-1), c-2**(n-1))
# return : 1,2,3,4 (몇사분면인지 알려준다.)
def find_q(n, r, c):

    num = 2**(n-1)

    # 해당 함수는 몇사분면 위인가?
    if (r < num) & (c < num): # 1사분면
        return 0
    elif (r < num) & (c >= num): # 2사분면
        return 1
    elif (r >= num) & (c < num): # 3사분면
        return 2
    else: # 4사분면
        return 3

n, r, c = map(int, input().split())

print(find_num(n, r, c))