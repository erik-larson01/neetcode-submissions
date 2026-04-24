class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, currentSubset):
            # Base case
            if i == len(nums):
                res.append(currentSubset.copy())
                return
            
            # Add the next number and continue
            currentSubset.append(nums[i])
            dfs(i + 1, currentSubset)
            currentSubset.pop() # Backtrack

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            # Recurse on next unique index
            dfs(i + 1, currentSubset)
 
        nums.sort()
        dfs(0, [])
        return res