# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # We need to split the list in two, then reverse the second half of the list

        # 1. Find midpoint and split
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        secondHalf = slow.next
        slow.next = None # Split into two parts

        # 2. Reverse second list
        prev = None
        while secondHalf:
            temp = secondHalf.next
            secondHalf.next = prev

            prev = secondHalf
            secondHalf = temp

        # Interleave nodes
        firstHalf, secondHalf = head, prev
        while secondHalf:
            temp1, temp2 = firstHalf.next, secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = temp1
            firstHalf, secondHalf = temp1, temp2

