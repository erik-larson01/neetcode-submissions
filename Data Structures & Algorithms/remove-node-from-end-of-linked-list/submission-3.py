# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Remove Length - n ListNode
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        indexToRemove = length - n
        if indexToRemove == 0:
            return head.next
        
        curr = head
        for i in range(length - 1):
            if (i + 1) == indexToRemove:
                curr.next = curr.next.next # Skip over
                break
            curr = curr.next
        
        return head