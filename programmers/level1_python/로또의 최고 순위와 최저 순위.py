def solution(lottos, win_nums):
    check = 0
    non_check = 0
    for i in lottos:
        
        # 알아본경우
        if i != 0:
            if i in win_nums:
                check += 1
        else:
            non_check +=1
    
    # 맞춘 갯수가 0 ~ 6개순서
    rank = [6,6,5,4,3,2,1]
    max_check = check + non_check
    answer = []
    answer.append(rank[max_check])
    answer.append(rank[check])
    
    return answer


if __name__ == "__main__":
    
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    
    # [3,5]
    
    print(solution(lottos, win_nums))