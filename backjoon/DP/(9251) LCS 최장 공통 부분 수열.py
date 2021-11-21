"""
LCS
https://www.acmicpc.net/problem/9251
"""
import sys
sys.setrecursionlimit(10**5)


first_word = input()
first_word_len = len(first_word)

second_word = input()
second_word_len = len(second_word)




data = [[0] * second_word_len for _ in range(first_word_len)]
max_data = []


for i, first in enumerate(first_word):

    for j, second in enumerate(second_word):

        if first == second:
            data[i][j] = 1

def dd(x,x_max,check_x, y, y_max, check_y, data, result):

    if data[x][y] == 1:
        check_x = x
        check_y = y
        result+=1
        cal_x = x+1
        cal_y = y+1
        # 마지막 x_max, y_max 값 비교를 위해
        if cal_x== x_max and cal_y == y_max:
            if data[cal_x-1][cal_y-1] == 1:
                return result+1
            else:
                return result

        if cal_x == x_max:
            cal_x = x_max-1
        if cal_y == y_max:
            cal_y = y_max-1

        return dd(cal_x,x_max,check_x,  cal_y, y_max, check_y, data, result)

    else:

        cal_x = x
        cal_y = y+1
        if cal_y == y_max:
            cal_x = x + 1
            if cal_x == x_max and cal_y == y_max:
                if data[cal_x - 1][cal_y - 1] == 1:
                    return result + 1
                else:
                    return result

            cal_y = check_y+1


        if cal_x == x_max:
            cal_x = x_max-1
        if cal_y == y_max:
            cal_y = y_max-1

        return dd(cal_x, x_max, check_x, cal_y, y_max, check_y,  data, result)


for i in range(first_word_len):
    for j in range(second_word_len):

        max_data.append(dd(i,first_word_len,0, j, second_word_len, 0, data, 0))

print(max(max_data))
