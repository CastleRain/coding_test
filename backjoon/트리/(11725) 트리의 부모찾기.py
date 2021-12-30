"""
https://www.acmicpc.net/problem/11725

일단 처음에는 못풀었다. dic을 이용해서 할까 생각했지만 어떤게 루트인지 확인이 불가했다.

블로그를 확인하고 dfs를 이용한다는것까지 확인을 했는데.. dfs를 활용해서 어케푸는거지

"""

import sys
input = sys.stdin.readline



n = int(input())

data = [[] for i in range(n+1)]
result = [[] for i in range(n+1)]
check = []

# val : 부모노드
# check_list : 부모들 저장되있는곳
# result : 
def find_parent(val, check_list, data, result):
    
    # 자식이 없으면 패스한다.
    if len(data[val]) != 0:

        # 자식이 있는 경우 해당 자식의 부모가 누군지 등록한다.
        for i in data[val]:

            # 부모노드들은 뺀다.
            if i not in check_list:
                
                # 부모노드가 되었으므로 추가한다.
                check_list.append(i)

                # 부모를 등록한다.
                result[i] = val

            # 자식도 반복을 진행한다.
                find_parent(i, check_list, data, result)

for _ in range(n-1):

    a, b = map(int, input().split())

    data[a].append(b)
    data[b].append(a)

find_parent(1, check, data, result)

for i in range(2, n+1):
    print(result[i])




    
    




# for i in range(1, n+1):
#     for j in data[i]:
#         result[j] = i
# class Parent_Node():
#     def __init__(self, data):

#         self.data = data
#         self.left = None
#         self.right = None
#         self.parent = None


# a = Parent_Node(1)
# a.left = Parent_Node(2)

# a.right = 3

