"""
피보나치 수 5
https://www.acmicpc.net/problem/10870

"""

def fibo(x):
    if x == 0:
        return 0
    if x in [1,2]:
        return 1

    return fibo(x-1) + fibo(x-2)

x = int(input())
print(fibo(x))