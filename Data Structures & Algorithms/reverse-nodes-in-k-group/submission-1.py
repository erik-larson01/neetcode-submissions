# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # Make a pointer to the node just before the current group
        prevGroupEnd = dummy

        while True:
            # Get kth value from groupPrev
            kthValue = self.getKthValue(prevGroupEnd, k)
            if not kthValue:
                break
            nextGroupStart = kthValue.next

            # Reverse this group of k nodes
            prev, curr = nextGroupStart, prevGroupEnd.next
            while curr != nextGroupStart:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # Connect ending pointers
            temp = prevGroupEnd.next
            prevGroupEnd.next = kthValue
            prevGroupEnd = temp
        return dummy.next


    
    def getKthValue(self, curr, k):
        while curr and k > 0:
            k -= 1
            curr = curr.next
        return curr