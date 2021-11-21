"""
나누기
"""

n = int(input())
m = int(input())

result = 100
for i in range(100):

    list_n = list(str(n))
    last_data = str(i).zfill(2)

    list_n[-2:] = last_data

    int_n = int(''.join(list_n))

    if int_n % m == 0:
        if result > i:
            result = i
print(str(result).zfill(2))

# print(f"n = {n}")
# print(f"m = {m}")