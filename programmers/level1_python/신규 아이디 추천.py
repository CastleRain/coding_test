# re 없이

def solution(new_id):

    # 1
    new_id = str(new_id.lower())

    # 2
    compare_list = ['-', '_', '.']
    id_list = []
    for i in new_id:
        if i.isalpha() or i.isdigit():
            id_list.append(i)
        elif i in compare_list:
            id_list.append(i)

    new_id = "".join(map(str, id_list))

    # 3    

    while new_id.find("..") != -1:
        new_id = new_id.replace("..", ".")


    while True:
        if len(list(new_id)) != 0:
            if new_id[-1:] == ".": 
                new_id = new_id[:-1]
            elif new_id[0] ==".":
                new_id = new_id[1:]
            else:
                break
        else:
            if len(list(new_id)) == 0:
                new_id = "a"

    # 6
    if len(list(new_id)) >= 16:
        new_id = new_id[:15]

    while True:
        if len(list(new_id)) != 0:
            if new_id[-1:] == ".": 
                new_id = new_id[:-1]
            elif new_id[0] ==".":
                new_id = new_id[1:]
            else:
                break
        else:
            if len(list(new_id)) == 0:
                new_id = "a"




    while len(list(new_id)) <= 2:
        new_id += new_id[-1]

    return new_id

# import re

# def solution(new_id):
#     st = new_id
#     st = st.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)
#     st = re.sub('\.+', '.', st)
#     st = re.sub('^[.]|[.]$', '', st)
#     st = 'a' if len(st) == 0 else st[:15]
#     st = re.sub('^[.]|[.]$', '', st)
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#     return st


if __name__ == "__main__":
    
    new_id = "...!@BaT#*..y.abcdefghijklm"

    
    # "bat.y.abcdefghi"
    
    print(solution(new_id))