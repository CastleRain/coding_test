import math


# data = [0] * (1024 * 1024 + 1) 

n, m = map(int, input().split())
# data = [0] * (2**math.ceil(math.log2(n)) + 1)
data = [0] * (n+1)

def tree(duck):

    if duck > n:
        return
    elif data[duck] == 1:
        return
    data[duck] = 1

    tree(duck*2)
    tree(duck*2+1)


for _ in range(m):
    duck = int(input())
    
    # 이런 경우는 없는듯?
    # if duck > n:
    #     print()
    cnt = 1
    
    if data[duck] == 0:
        print(0)
        tree(duck)

    else: # 부모 찾아 나가자
        while True:
            if data[duck//2] == 0:
                print(duck)
                break
            duck //= 2
            
            if duck == 1:
                break

            



