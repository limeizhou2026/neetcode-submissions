# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        #要读fast.next就必须fast是valid node；同样的 fast.next也是一个道理
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


        if not head:
            return False
        
        seen = set()
        curr = head
        while curr:
            if curr not in seen:
                seen.add(curr)
            else:
                return True
            curr = curr.next

        return False










































        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False       