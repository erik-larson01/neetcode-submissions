class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(permutation, nums, isPicked):
            if len(permutation) == len(nums):
                # Save permutation
                res.append(permutation.copy())
                return
            for i in range(len(nums)):
                # Check if element is in permutation
                if isPicked[i] == False:
                    # Add to permutation and recurse
                    isPicked[i] = True
                    permutation.append(nums[i])
                    backtrack(permutation, nums, isPicked)

                    # Undo addition and continue
                    isPicked[i] = False
                    permutation.pop()
        
        backtrack([], nums, [False] * len(nums))
        return res