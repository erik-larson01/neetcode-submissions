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
            # Save the next node
            temp = curr.next

            # Reverse the pointer
            curr.next = prev

            # Move prev to curr and curr to temp (advance pointers)
            prev = curr
            curr = temp
        return prev