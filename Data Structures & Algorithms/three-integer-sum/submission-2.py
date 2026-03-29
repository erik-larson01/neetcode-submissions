class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Sort to help skip duplicates
        nums.sort()

        for i, a in enumerate(nums):
            # Check if the starting value "a" is not the same as its predecessor
            if i > 0 and a == nums[i - 1]:
                continue
            
            # "A" is fixed, now do TwoSumII with B and C
            l, r = i + 1, len(nums) -1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # Inc l for no duplicates - keep going until it is not the same as pred
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res