"""
https://www.acmicpc.net/problem/2553


"""

n = int(input())

result = 1
for i in range(1, n+1):

    result *= i
    # print("i = ", i)
    # print("result = ", result)
    
    # result에서 0이 아닌 첫번째 숫자 가져오기
    if int(str(result)[-1]) == 0:
        for k in range(len(str(result))):

            if int(str(result)[-(k+1)]) != 0:

                result = int(str(result)[:-(k)])
                break
    if len(str(result)) > 11:
        result %= 10000000000
    # print("i = ", i)
    # print("result = ", result)
    # print("++++++++++++++++++++")

    


print(result%10)


