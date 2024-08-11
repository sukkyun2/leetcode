# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans, cur_ans = None, None
        cur1, cur2 = list1, list2

        def add_value(ans, cur, val):
            if ans is None:
                ans = ListNode(val)
                cur = ans
            else:
                cur.next = ListNode(val)
                cur = cur.next

            return ans, cur

        while cur1 and cur2:
            if cur1.val >= cur2.val:
                ans, cur_ans = add_value(ans, cur_ans, cur2.val)
                cur2 = cur2.next
            elif cur1.val < cur2.val:
                ans, cur_ans = add_value(ans, cur_ans, cur1.val)
                cur1 = cur1.next

        while cur1:
            ans, cur_ans = add_value(ans, cur_ans, cur1.val)
            cur1 = cur1.next

        while cur2:
            ans, cur_ans = add_value(ans, cur_ans, cur2.val)
            cur2 = cur2.next

        return ans
