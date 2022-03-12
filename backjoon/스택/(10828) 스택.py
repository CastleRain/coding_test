"""
https://www.acmicpc.net/problem/10828

"""

n = int(input())

stack = []
for _ in range(n):

    m = input()
    # push
    if "push" in m:
        stack.append(int(m[5:]))
    elif "pop" in m:
        if len(stack) > 0:
            print(stack.pop())
        else:
            print("-1")
    elif "size" in m:
        print(len(stack))
    elif "empty" in m:
        if len(stack) > 0:
            print("0")
        else:
            print("1")
    else:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print("-1")
