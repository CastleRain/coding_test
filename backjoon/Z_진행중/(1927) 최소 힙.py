"""
https://www.acmicpc.net/problem/1927

"""



# import heapq

# queue = []
# n = int(input())


# for _ in range(n):
#     data = int(input())
#     if data:
#         heapq.heappush(queue, data)
#     else:
#         if len(queue) != 0:
#             print(heapq.heappop(queue))
#         else:
#             print(0)

# class heap:
    
#     def __init__(self):
#         self.data = []
        

    
#     def add(self, num):
#         self.data.append(num)
#         self.min_data = min(self.min_data, num)
        
        
    
#     def pop(self):
#         if len(self.data) == 0:
#             print(0)
#         else:
#             print(self.min_data)
#             self.data.remove(self.min_data)

# h = heap()
# for _ in range(n):
#     data = int(input())
#     if data:
#         h.add(data)
#     else:
#         h.pop()

