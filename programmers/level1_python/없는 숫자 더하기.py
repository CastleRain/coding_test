def solution(numbers):
    
    
    data = [i for i in range(10)]
    
    for i in set(numbers):
        data.remove(i)
    answer = sum(data)
    
    
    
    
    return answer

if __name__ == "__main__":
    
    numbers = [1,2,3,4,6,7,8,0]

    
    print(solution(numbers))