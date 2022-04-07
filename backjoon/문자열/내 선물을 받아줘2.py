"""
1, x위치
2. E에 가면 오른쪽으로 이동
3. W에 가면 왼쪽으로 이동

구사과의 위치를 모른다. 이동 시작하는 위치와 관계없이 선물을 주고싶다.

"""

n = int(input())
data = input()

cnt = 0
check_E = -1
check_W = -1

while check_W != n-1:
    if data[check_W+1:].find("E") == -1:
        break
    
    check_E = data[check_W+1:].find("E") + check_W + 1
    check_W = data[check_E+1:].find("W") + check_E + 1
    cnt += 1
print(cnt)

