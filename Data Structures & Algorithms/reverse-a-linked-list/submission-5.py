# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive
        def reverse(cur, prev):
            # base case
            if cur is None:
                return prev
            else:
                temp = cur.next
                cur.next = prev
                return reverse(temp, cur)

        return reverse(head, None)