class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, currPerm, isPicked):
            if len(nums) == len(currPerm):
                res.append(currPerm.copy())
                return
            for i in range(len(nums)):
                if not isPicked[i]:
                    currPerm.append(nums[i])
                    isPicked[i] = True

                    backtrack(nums, currPerm, isPicked)
                    currPerm.pop()
                    isPicked[i] = False

        backtrack(nums, [], [False] * len(nums))
        return res