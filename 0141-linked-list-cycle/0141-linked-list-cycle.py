# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        def move(node):
            if not node:
                return None
            
            return node.next
        
        if not head:
            return False
        
        slow = move(head.next)
        fast = move(move(head.next))
        
        while slow and fast:
            if slow == fast:
                return True

            slow = move(slow)
            fast = move(move(fast))

        return False