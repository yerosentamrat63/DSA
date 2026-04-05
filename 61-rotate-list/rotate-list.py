# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = head
        if not head:
            return head
        count = 1
        
        while dummy.next:
            dummy = dummy.next
            count += 1
        
        pos = k % count
        if pos == 0:
            return head
        
        curr = head

        for i in range(count - pos - 1):
            curr = curr.next
        
        newHead = curr.next
        curr.next = None
        dummy.next = head

        return newHead