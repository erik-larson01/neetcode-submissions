class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Brute force
        res = nums[0]
        for i in range(len(nums)):
            curr = nums[i]
            res = max(res, curr) # Handle subarrays of len 1
            for j in range(i + 1, len(nums)):
                curr *= nums[j]
                res = max(res, curr)
        return res