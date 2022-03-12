"""
https://www.acmicpc.net/problem/16987

"""
import copy

def solution(data, num):
    global max_break
    data_copy = copy.deepcopy(data)
    # 만약 오른쪽 끝이라면 return
    if len(data) == num+1:
        cnt = 0
        for f_data, s_data in data:
            if f_data <= 0:
                cnt += 1
        max_break = max(max_break, cnt)
        return
    
    # 자기 자신을 제외한 나머지 알들을 쳐야하는데 w가 0이면 안된다.
    for i in range(len(data)):
        #자기 자신이 아닐 때, w가 0보다 클때
        data = copy.deepcopy(data_copy)

        if (i != num) and (data_copy[i][0] > 0):
            
            # 쳐본다. 
            data[num][0], data[i][0] =  data[num][0] - data[i][1], data[i][0] - data[num][1]


            # 자기 자신으로부터 0이 아닌 최고 오른쪽 값을 가져온다. 만약 아무것도 없다면 제일 끝값을 넣어준다.
            check = True
            for k in range(num+1,len(data)):
                if data[k][0] > 0:
                    check = False
                    solution(data, k)
            if check:
                solution(data, len(data)-1)




if __name__ == "__main__":


    n = int(input())

    max_break = 0

    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))
    
    solution(data,0)

    print(max_break)