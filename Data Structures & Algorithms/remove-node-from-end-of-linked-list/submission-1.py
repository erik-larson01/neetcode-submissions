# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        # this works because the node to remove is exactly n nodes from the end
        
        # Advance left n spaces forward
        count = 0
        while count < n:
            count += 1
            right = right.next
        
        # Advance both
        while right:
            left = left.next
            right = right.next
        
        # Skip over left.next
        left.next = left.next.next
        return dummy.next
        
        