class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() # Sort list to easily skip duplicates
        def dfs(i, currentList, total):
            # If the target has been reached, add the combination to the result array
            if total == target:
                res.append(currentList.copy())
                return
            # Stop exploring the tree if index is at the end or the total has been exceeded
            if i == len(candidates) or total > target:
                return
            
            # Include the current number
            currentList.append(candidates[i])
            dfs(i + 1, currentList, total + candidates[i])

            # Backtrack: Exclude the current number
            currentList.pop() # Reset the currentList to its previous state

            # Skip duplicates to exclude duplicates of that number
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i +=1
            dfs(i + 1, currentList, total)
        dfs(0, [], 0)
        return res