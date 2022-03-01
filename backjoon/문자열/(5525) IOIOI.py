"""
https://www.acmicpc.net/problem/5525


IOI => 몇번 반복하는지 
첫번째 IOI가 나오면 그다음부턴 OI나올떄마다 +1
끊기면 x

"""
import sys

input = sys.stdin.readline

n = int(input())
m = input()
data = input()

data_cnt = []
index = -1
while True:
    index = data.find("IOI", index+1)
    if index == -1:
        break
    data_cnt.append(index)

cnt = 0
data_result = []
for d in data_cnt:
    if cnt == 0:
        last_data = d
        cnt += 1
    else:
        if last_data == d-2:
            last_data = d
            cnt += 1
        else:
            last_data = d
            data_result.append(cnt)
            cnt = 1
data_result.append(cnt)
result = 0
for i in data_result:
    if (i-n+1) >= 0:
        result += (i-n+1)

print(result)
    
