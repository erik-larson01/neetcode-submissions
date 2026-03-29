class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_set = set()
        for num in nums:
            new_set.add(num)    
        return len(new_set) != len(nums)
        