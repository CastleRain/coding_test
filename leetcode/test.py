

for i, cur in enumerate(temperatures):
    while stack and cur > temperatures[stack[-1]]:
        last = stack.pop()
        answer[last] = i - last

    stack.append(i)