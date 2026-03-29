class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                # Section is sorted, simply return min 
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[l] <= nums[m]:
                # L and M are in same group
                l = m + 1
            else:
                # M and R are in same group
                r = m - 1
        return res
