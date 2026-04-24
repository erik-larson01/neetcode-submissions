class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, currentSubset):
            if i == len(nums):
                res.append(currentSubset.copy())
                return
            
            currentSubset.append(nums[i])
            dfs(i + 1, currentSubset)
            currentSubset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, currentSubset)
 
        nums.sort()
        dfs(0, [])
        return res