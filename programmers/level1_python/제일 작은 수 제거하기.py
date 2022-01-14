def solution(arr):
    
    
    arr.remove(min(arr))
    
    if len(arr) ==0:
        return [-1]
    else:
        return arr

if __name__ == "__main__":
    
    arr = [4,3,2,1]

    # [4,3,2]
    
    print(solution(arr))