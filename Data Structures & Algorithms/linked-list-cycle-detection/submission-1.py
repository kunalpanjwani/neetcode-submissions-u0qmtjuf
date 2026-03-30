# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a = set()
        # prev, curr = None, head
        while head:
            if head in a:
                return True
            a.add(head)
            head = head.next
        return False

