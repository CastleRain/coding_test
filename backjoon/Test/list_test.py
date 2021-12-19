<<<<<<< HEAD
import collections

root = [1,2,3,4,5]
q = collections.deque([root])

print(q)
=======
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
>>>>>>> 6dafc79ab4c058ea36625e4394c37d847869d9b4
