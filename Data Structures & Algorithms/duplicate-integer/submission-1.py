class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_set = set()
        for num in nums:
            if num in new_set:
                return True
            new_set.add(num)    
        return False
        