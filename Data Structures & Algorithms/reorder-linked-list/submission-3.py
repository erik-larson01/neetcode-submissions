# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find midpoint
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split list into two parts
        second = slow.next
        slow.next = None

        # Reverse second list
        prev = None
        while second:
            temp = second.next
            second.next = prev

            prev = second
            second = temp
        
        # Interleave nodes
        first, second = head, prev # Start of respective lists
        while second:
            tempFirst, tempSecond = first.next, second.next
            first.next = second
            second.next = tempFirst
            first, second = tempFirst, tempSecond
