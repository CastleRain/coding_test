"""

created : 22.01.14
by CastleRain

"""

def solution(numbers):

    # n이 100이므로 for for 돌아도 10000번이다. 충분하다.
    answer = []

    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    
    return sorted(list(set(answer)))


if __name__ == "__main__":
    
    numbers = [100, 100, 100, 99, 98]

    # [2,3,4,5,6,7]
    
    print(solution(numbers))