# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find length of list
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        # Now find node length - n from the end
        indexToRemove = length - n
        if indexToRemove == 0:
            return head.next
        
        # Skip over node at indexToRemove
        curr = head
        for i in range(length - 1):
            if (i + 1) == indexToRemove:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head
            