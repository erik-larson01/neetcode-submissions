class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        already_seen = set()

        for n in nums:
            if n in already_seen:
                return True
            already_seen.add(n)
        return False