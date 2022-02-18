"""
https://programmers.co.kr/learn/courses/30/lessons/81301

"""

def change_num(number):
    dic_data = ["zero", "one", "two", 'three','four','five','six','seven','eight','nine']
    result = []
    num = []
    for i in number:
        num.append(i)
        if ''.join(num) in dic_data:
            result.append(str(dic_data.index(''.join(num))))
            num = []
    return ''.join(result)





def solution(s):
    answer = []
    alpha = ""
    for i in s:
        if i.isdigit():
            if len(alpha) != 0:
                answer.append(change_num(alpha))
                alpha = ""
            answer.append(i)
        else:
            alpha += i
    if len(alpha) != 0:
        answer.append(change_num(alpha))


    return int(''.join(answer))



s = "23four5six7"

print(solution(s))


"""
다른사람 풀이

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)



"""