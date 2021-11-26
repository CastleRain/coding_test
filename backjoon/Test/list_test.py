n = input()
result = 0

if len(n) == 2:
    for i in n:
        result += int(i)
elif len(n) == 4:
    result = 20
else:
    if n[1] == "0":
        result = 10 + int(n[2])
    else:
        result = 10 + int(n[0])

print(result)