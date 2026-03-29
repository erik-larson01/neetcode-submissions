# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        # Find midpoint of list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        list2 = slow.next

        # Split the list into two halves
        slow.next = None

        # Reverse list2
        prev = None
        while list2:
            temp = list2.next
            list2.next = prev
            prev = list2
            list2 = temp

        # Combine the two lists (prev is now head of reversed list2)
        list1, list2 = head, prev
        while list2:
            temp1, temp2 = list1.next, list2.next
            list1.next = list2
            list2.next = temp1
            list1, list2 = temp1, temp2
            
