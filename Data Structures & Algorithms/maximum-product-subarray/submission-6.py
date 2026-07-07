class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = 1
        currMin = 1
        res = nums[0]

        for num in nums:
            temp = currMax * num
            currMax = max(currMax * num, currMin * num, num)
            currMin = min(temp, currMin * num, num)
            res = max(res, currMax)
        return res