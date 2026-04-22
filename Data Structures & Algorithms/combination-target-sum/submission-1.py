class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, currentList, total):
            # If the target has been reached, add the combination to the result array
            if total == target:
                res.append(currentList.copy())
                return
            # Stop exploring the decision tree
            if i == len(nums) or total > target:
                return
            
            # Include the current number (i does not change so the number can be reused)
            currentList.append(nums[i])
            dfs(i, currentList, total + nums[i])
            # Backtrack: Exclude the current number
            currentList.pop() # Reset the currentList to its previous state
            dfs(i + 1, currentList, total)
        dfs(0, [], 0)
        return res