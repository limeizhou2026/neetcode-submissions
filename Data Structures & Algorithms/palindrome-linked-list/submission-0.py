# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        cur = head

        while cur:
            stack.append(cur.val)
            cur = cur.next
        
        cur = head
        while cur and cur.val == stack.pop():
            cur = cur.next

        return not cur

        