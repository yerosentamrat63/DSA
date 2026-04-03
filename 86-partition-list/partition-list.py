# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        low_dummy  = ListNode(0)
        high_dummy = ListNode(0)
        low  = low_dummy
        high = high_dummy

        curr = head
        while curr:
            if curr.val < x:
                low.next = curr
                low = low.next
            else:
                high.next = curr
                high = high.next
            curr = curr.next

        high.next = None
        low.next = high_dummy.next

        return low_dummy.next