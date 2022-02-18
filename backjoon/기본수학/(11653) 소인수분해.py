"""
https://www.acmicpc.net/problem/11653

"""

n = int(input())
i = 2
k = int(n**0.5)+1

while( i < k ):
    if n % i == 0:
        print(i)
        n /= i
    else:
        i += 1
    
    if n == 1:
        break

if n != 1:
    print(int(n))
