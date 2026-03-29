# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # To reverse the list, we need to create a temp node 
        # and then reverse the actual next nodes pointer
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev

            # Move pointers forward
            prev = curr
            curr = temp
        
        return prev