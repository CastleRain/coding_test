data = [13, 15, 14,  17, 18, 16, 16]
d = 2
k = 1

answer = []

del_count = 0
pre_data = 0

for i, da in enumerate(data):

    if i == 0 :
        answer.append(da)
        continue

    if pre_data == 0:
        pre_data = da
    else:
        if del_count > k:
            answer.append(pre_data)
            pre_data = da
            del_count = 0

        else:
            if abs(pre_data - da) <= d:
                del_count += 1
                pre_data = da
            else:
                del_count = 0
                answer.append(pre_data)
                pre_data = da

    if len(data)- 1 == i:
        answer.append(da)
print(answer)


