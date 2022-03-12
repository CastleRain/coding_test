"""
https://www.acmicpc.net/problem/1672

"""


# A = 0, G = 1, C =2, T= 3
data = [['A', 'C','A','G'],['C','G','T','A'], ['A','T','C','G'], ['G','A','G','T']]

dna = ['A', 'G', 'C', 'T']
input()
input_data = list(input())

stack = []
while len(input_data) > 0:
    stack.append(input_data.pop())

    if len(stack) == 2:
        
        first = stack.pop()
        second = stack.pop()

        stack.append(data[dna.index(first)][dna.index(second)])

print(stack[0])
