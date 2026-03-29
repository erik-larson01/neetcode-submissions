class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            # There are 2 sorted sections
            if nums[l] <= nums[m]:
                # Left half is sorted, search right
                l = m + 1
            else:
                # Right half is sorted as nums[m] < nums[r]
                r = m - 1
        return res