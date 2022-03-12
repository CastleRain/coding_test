def solution(arr):
    answer = []
    last_word = ''
    for i in arr:
        if i != last_word:
            answer.append(i)
            last_word = i
    

    return answer


if __name__ == "__main__":
    
    arr = [1,1,3,3,0,1,1]	


    # [1,3,0,1]

    
    print(solution(arr))