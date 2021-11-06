"""

크로아티아 알파벳
https://www.acmicpc.net/problem/2941


"""
def check_cro(word):
    cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    if word in cro_alpha:
        return 1
    else:
        return 0




word = input()

#최대 3개까지 확인을 진행해야한다.

count = 0
save_word = ""
# 크로아티아 단어가 나오게되면 현재 위치로 복귀
for w in word:

    save_word += w

    #저장된 단어가 4인경우는 확인불가
    if len(save_word) == 4:
        save_word = save_word[1:]
        count+=1

    if len(save_word)>=2 and len(save_word)<4:

        if check_cro(save_word):
            save_word = ""
            count +=1
        else:
            if check_cro(save_word[:2]):
                if len(save_word) == 3:
                    save_word = save_word[2]
                    count += 1
                else:
                    save_word = ""
                    count += 1

# 마지막으로 남은 단어 정리
while len(save_word):
    if check_cro(save_word):
        save_word = ""
        count += 1
    else:
        save_word = save_word[1:]
        count+=1

print(count)