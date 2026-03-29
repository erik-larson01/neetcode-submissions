class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Treat array like linked List
        slow, fast = 0,0 

        # Find cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # Cycle found at index slow
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow