"""
연결리스트가 팰린드롬 구조인지 판별하기

1->2
false

1->2->2->1
true

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

ListNode는 다음과 같이 정의가 되어져있는상태이다.

"""
# 방법 1

#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         q: List = []
#
#         if not head:
#             return True
#
#         node = head
#
#         while node is not None:
#             q.append(node.val)
#             node = node.next
#
#         while len(q) > 1:
#             if q.pop(0) != q.pop():
#                 return False
#         return True

#방법 2
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         q: Deque = collections.deque()
#
#         if not head:
#             return True
#
#         node = head
#
#         while node is not None:
#             q.append(node.val)
#             node = node.next
#
#         while len(q) > 1:
#             if q.popleft() != q.pop():
#                 return False
#
#         return True

#방법 3
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev