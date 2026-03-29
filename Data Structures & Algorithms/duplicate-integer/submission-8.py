class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        already_seen = set()

        # Use seen array to keep track of values seen before
        for n in nums:
            if n in already_seen:
                return True
            already_seen.add(n)
        return False