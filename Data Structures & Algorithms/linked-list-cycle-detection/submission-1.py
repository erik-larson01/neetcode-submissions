# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Use fast/slow pointer approach
        slowPtr = fastPtr = head

        while fastPtr and fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            if slowPtr == fastPtr:
                # There is a cycle
                return True
        return False