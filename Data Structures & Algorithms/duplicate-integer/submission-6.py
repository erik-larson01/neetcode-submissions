class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_set = set()

        for n in nums:
            duplicate_set.add(n)
            if n not in duplicate_set:
                return True
        return True if len(duplicate_set) != len(nums) else False     