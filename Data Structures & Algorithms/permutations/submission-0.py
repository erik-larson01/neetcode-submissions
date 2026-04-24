class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(permutation, nums, isPicked):
            # Base case
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return
            for i in range(len(nums)):
                if not isPicked[i]:
                    # Value is not in the permutation, add it and continue
                    permutation.append(nums[i])
                    isPicked[i] = True
                    backtrack(permutation, nums, isPicked)
                    # Undo the addition and continue
                    permutation.pop()
                    isPicked[i] = False
                    
        isPicked = [False] * len(nums)
        backtrack([], nums, isPicked)
        return res