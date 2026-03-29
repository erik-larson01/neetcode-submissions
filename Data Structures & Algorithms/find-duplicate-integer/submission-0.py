class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicates = set()
        for n in nums:
            if n in duplicates:
                return n
            duplicates.add(n)
        return -1