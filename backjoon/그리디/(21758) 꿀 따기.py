"""
https://www.acmicpc.net/problem/21758

꿀통이 끝에 위치하거나 벌들이 끝에 위치해야함

1) 양쪽 끝에 벌이 위치 -> 꿀통은 중간에서 제일 큰값에 위치
2) 벌꿀통이 양쪽끝에 위치 -> 양쪽끝 중 값이 작은곳에 위치

누적합
"""
# 1)
def side_bee(data, sum_data):
    return sum_data[-2]-data[0] + max(data[1: -1])

# 2)
def side_honey(data, sum_data):
    max_honey = 0
    # 왼쪽에 집이 있는 경우 오른쪽 하나는 확정

    for i in range(1, len(data)-1):


        max_honey = max(max_honey, sum_data[i-1] + sum_data[-2] - data[i])

    # 오른쪽에 집이 있는 경우 왼쪽 하나는 확정

    for i in range(1, len(data)-1):
        

        max_honey = max( max_honey, (sum_data[-1] - data[0] - data[i]) + (sum_data[-1] - sum_data[i]))

    return max_honey




if __name__ == "__main__":


    n = int(input())
    data = list(map(int,input().split()))
    sum_data = []
    result = 0
    for i in data:
        result += i
        sum_data.append(result)

    # 꿀벌이 양쪽에 배치되어있을 떄 sum(data[1:-1]) + max(data[1: -1])
    # 
    print(max(side_bee(data, sum_data), side_honey(data, sum_data) ))

