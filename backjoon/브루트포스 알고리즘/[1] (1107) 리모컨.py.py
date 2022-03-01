"""
https://www.acmicpc.net/problem/1107

리모컨 숫자 0 ~ 9, +, -

0에서 -누르면 안 줄어들고 채널은 무한이있다.
이동하려고하는 채널은 N

어떤 버튼이 고장났는지 주어졌을 때 N으로 이동하기 위해서 버튼 최소 몇 번?

보고있는 채널 : 100

1. 100번에서 + - 로 얼마나 걸리는가?
2. 숫자로 바로 입력이 되는가?
    2.1 숫자로 가장 가까운 숫자 입력 후 + - 로 얼마나 걸리는가?

1, 2.1 비교


len이 작을 때 : 최댓값
len이 클 때 : 최솟값

len이 같을 때 : 최대한 비슷한 값
    1. 작은값 => 최대한 크게
    2. 큰값 => 최대한 작게
    3. 첫값과 같은 값
        두번째 값과 같은 값
        작은값 => 최대한 
        큰값 => 최대한 작게

"""

N = int(input())
ans = abs(100 - N) # ++ or -- 로 이동할 경우 -> 최댓값
M = int(input())
btn = [str(i) for i in range(10)]
if M != 0:
    for b in list(map(str, input().split())):
        btn.remove(b)

# 작은수에서 큰수로 이동할땐 500,000 까지만 보면 되지만
# 반대로 큰수에서 작은수로 내려올수도 있으므로 1,000,000 까지 봐야함
for num in range(1000001): 
    for i in str(num):
        if i not in btn: # 해당 숫자가 번호를 눌러서 만들 수 없는 경우엔 스탑
            break
    else: # 번호를 눌러서 만들 수 있는 경우엔
    	# min(기존답, 번호를 누른 횟수 + 해당 번호로부터 타겟까지의 차이)
        ans = min(ans, len(str(num)) + abs(num - N))

print(ans)




# N = str(input())
# M = int(input())
# btn = [i for i in range(10)]
# if M != 0:
#     for b in list(map(int, input().split())):
#         btn.remove(b)

# min_data = 1e9

# def solution(find_num:str, min_data):
#     select_num = ""
#     # 찾는 단어 하나하나 진행
#     for i in find_num:
        
#         # 버튼에 있는 단어인지 확인
#         if int(i) in btn: #버튼에 있는 단어라면
            
#             select_num += str(i) # 찾은 단어에 해당 번호를 입력해준다.
               
#         else:# 버튼에 없는 단어라면

#             min_num = -1
#             max_num = 10

#             find_num_min = select_num
#             find_num_max = select_num

#             for bt in btn:
#                 if bt < int(i):
#                     min_num = max(bt, min_num)
#                 elif bt > int(i):
#                     max_num = min(bt, max_num)

#             if min_num != -1: # 작은 수 
#                 find_num_min += str(min_num)

#                 if len(find_num_min) != len(N):
#                     find_num_min += (len(N) - len(find_num_min)) * str(btn[-1])

#                 if abs(int(N)-min_data) > abs(int(N)-int(find_num_min)):
#                     min_data = int(find_num_min)
            
#             if max_num != 10: # 큰 수

#                 find_num_max += str(max_num)
#                 if len(find_num_max) != len(N):
#                     find_num_max += (len(N) - len(find_num_max)) * str(btn[0])


#                 if abs(int(N)-min_data) > abs(int(N)-int(find_num_max)):
#                     min_data = int(find_num_max)
#             return min_data
    
#     return int(select_num)


# if int(N) == 100:
#     print(0)
# elif len(btn) == 0:
#     print(abs(int(N)-100))
# else:
#     result = ""
#     for _ in range(len(N)-1):
        
#         result += str(btn[-1])
#     if len(result) != 0:
#         if abs(int(N)-min_data) > abs(int(N)-int(result)):
#             min_data = int(result)

            
#     result = ""
#     for num, _ in enumerate(range(len(N)+1)):
#         if num == 0:
#             if ( btn[0] == 0) and ( len(btn) != 1):
#                 result += str(btn[1])
#             else:
#                 result += str(btn[0])
#         else:
#             result += str(btn[0])
#     if len(result) != 0:
#         if abs(int(N)-min_data) > abs(int(N)-int(result)):
#             min_data = int(result)

    


#     select_data = solution(N, 1e9) # 제일 작은 수 가져왔다.

#     if abs(int(N)-min_data) > abs(int(N)-int(select_data)):
#         min_data = int(select_data)

#     if abs(int(N) - min_data) + len(str(min_data)) < abs(int(N) - 100):
#         print(abs(int(N) - min_data) + len(str(min_data)))
#     else:
#         print(int(N) - 100)


