class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        current_subset = []

        def dfs(index):
            if index == len(nums):
                res.append(current_subset.copy())
                return
            # Form a decision tree by both including and skipping nums[index]
            current_subset.append(nums[index])
            dfs(index + 1)
            # Backtrack
            current_subset.pop()
            dfs(index + 1)
        dfs(0)
        return res

