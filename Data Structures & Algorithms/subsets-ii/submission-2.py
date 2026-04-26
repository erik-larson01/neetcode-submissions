class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, currSubset):
            if i == len(nums):
                res.append(currSubset.copy())     
                return
            
            currSubset.append(nums[i])
            dfs(i + 1, currSubset)
            
            currSubset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            dfs(i + 1, currSubset)
        dfs(0, [])
        return res