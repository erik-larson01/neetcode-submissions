# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Midpoint is now the slow pointer
        list2 = slow.next
        slow.next = None
        # Ordering of 1, n-1 is start of list1, last of list2
        # Reverse list2:
        prev = None
        while list2:
            temp = list2.next
            list2.next = prev

            prev = list2
            list2 = temp
        
        list1, list2 = head, prev
        while list2:
            temp1, temp2 = list1.next, list2.next
            list1.next = list2
            list2.next = temp1
            list1, list2 = temp1, temp2


        



