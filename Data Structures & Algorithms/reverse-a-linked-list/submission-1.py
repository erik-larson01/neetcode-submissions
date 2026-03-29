# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Set the curr pointer to the head and the prev value to None
        curr = head
        prev = None
        while curr:
            # The next node's next pointer needs to be the current node's prev
            temp = curr.next
            curr.next = prev

            # The new curr is the next node, and the prev value is set to the old curr
            prev = curr
            curr = temp
        return prev