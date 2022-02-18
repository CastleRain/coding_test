"""
https://www.acmicpc.net/problem/1652

"""

n = int(input())

data = []

row = 0
column = 0

def cnt_seat(data):
    result, cnt = 0, 0

    for i in data:
        if i == ".":
            cnt += 1
            if cnt == 2:
                result += 1   
        else:
            cnt = 0
    return result

for _ in range(n):
    d = input()
    row += cnt_seat(d)
    data.append(d)

for i in range(n):
    d = []
    for j in range(n):
        d.append(data[j][i])
    column += cnt_seat(d)        

print(row, column)
        


