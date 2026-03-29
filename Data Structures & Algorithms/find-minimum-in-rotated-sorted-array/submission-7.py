class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # Stops when l == r
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                # Right section is sorted, min must be in left
                r = m # Include mid
            else:
                # Left section is sorted, min must be in right
                l = m + 1 # Exclude mid
        return nums[l]