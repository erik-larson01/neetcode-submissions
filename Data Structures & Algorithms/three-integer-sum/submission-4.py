class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Check for duplicates
            if i > 0 and a == nums[i - 1]:
                continue
            l,r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # Three Sum = 0
                    res.append([a, nums[l], nums[r]])

                    # Advance to avoid duplicates
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res