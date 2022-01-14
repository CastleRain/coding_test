def gcd(x, y):
    
    if x < y:
        x, y = y, x
    
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
    

def solution(arr):
    
    # gcd 구하고 작은수랑 곱
    x = arr[0]
    
    for i in arr[1:]:

        x =  x * i / gcd(x, i)

        
    
    return x

if __name__ == "__main__":
    arr = [2,6,8,14]

    # 168

    print(solution(arr))