# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Instead of merging one at a time, simply pick smallest node over and over
        dummy = ListNode()
        cur = dummy

        while True:
            minNode = -1
            # Find min node
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if minNode == -1 or lists[minNode].val > lists[i].val:
                    minNode = i

            if minNode == -1:
                # No nodes are left
                break
            
            # Add minNode to list
            cur.next = lists[minNode]
            lists[minNode] = lists[minNode].next
            cur = cur.next

        return dummy.next