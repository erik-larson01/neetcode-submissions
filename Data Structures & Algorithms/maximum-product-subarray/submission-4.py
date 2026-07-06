class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax = 1 # So first multiplication does not change first num
        currMin = 1

        # Choose between staring over and extending prev best
        for num in nums:
            temp = currMax * num # Need old value when calc currMin

            # Extend from current max and min due to negatives
            currMax = max(num * currMax, num * currMin, num)
            currMin = min(temp, num * currMin, num)
            res = max(res, currMax)
        return res