"""
https://programmers.co.kr/learn/courses/30/lessons/67256
22.02.21

왼손과 오른손의 엄지만 이용해서 숫자만을 입력
왼쪽 엄지는 *
오른쪽 엄지는 #에서 시작

1,4,7 -> 왼쪽

3, 6, 9-> 오른쪽

2 5 8 0 -> 더 가까운 쪽

만약 거리가 같다면 오른손 잡이는 오른쪽 왼손잡이는 왼쪽이 먼저간다.

왼쪽과 오른쪽의 길이를 계속 구하고 확인하면 될듯?

"""



def solution(numbers, hand):
    answer =  ''
    
    keyboard = {
        1 : [0, 0],
        2 : [0, 1],
        3 : [0, 2],
        4 : [1, 0],
        5 : [1, 1],
        6 : [1, 2],
        7 : [2, 0],
        8 : [2, 1],
        9 : [2, 2],
        "*" : [3, 0],
        0 : [3, 1],
        "#" : [3, 2],
    }

    left = [1,4,7]
    right = [3,6,9]

    result = "L or R"

    # 현재 있는 위치를 저장하는 곳
    left_dir = "*"
    right_dir = "#"

    for num in numbers:
        
        # 왼쪽손으로 무조건 선택해야하는 경우
        if num in left:
            answer += "L"
            left_dir = num
        # 오른쪽손으로 무조건 선택해야 하는 경우
        elif num in right:
            answer += "R"
            right_dir = num         
        # 둘중 가까운 숫자를 골라야한다.
        else:
            left_num = abs((keyboard[left_dir][0] - keyboard[num][0])) + abs((keyboard[left_dir][1] - keyboard[num][1]))
            right_num = abs((keyboard[right_dir][0] - keyboard[num][0])) + abs((keyboard[right_dir][1] - keyboard[num][1]))

            if left_num < right_num:
                left_dir = num
                answer += "L"
            elif left_num == right_num:
                if hand == "left":
                    answer += "L"
                    left_dir = num
                else:
                    answer += "R"
                    right_dir = num
            else:
                right_dir = num
                answer += "R"

    return answer


numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

#"LRLLLRLLRRL"

print(solution(numbers, hand))