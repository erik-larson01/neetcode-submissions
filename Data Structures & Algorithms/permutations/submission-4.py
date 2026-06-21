class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, currPerm, picked):
            if len(currPerm) == len(nums):
                res.append(currPerm.copy())
            
            for i in range(len(nums)):
                if not picked[i]:
                    # Pick number
                    picked[i] = True
                    currPerm.append(nums[i])
                    backtrack(nums, currPerm, picked)
                    # backtrack
                    picked[i] = False
                    currPerm.pop()
        backtrack(nums, [], [False] * len(nums))
        return res