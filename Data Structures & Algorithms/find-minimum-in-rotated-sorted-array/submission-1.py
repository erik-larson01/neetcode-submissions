class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        result = nums[0]
        while l <= r:
            # Check if current window is already sorted
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break
        
            m = (l + r) // 2
            result = min(result, nums[m])
            # 2 of L, R and mid have to be in the same group
            if nums[m] >= nums[l]:
                # Mid is in left portion, search right
                l = m + 1
            else:
                # Mid is in right portion, search left
                r = m - 1
        return result