class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in nums:
        # Is it the start of a sequence?
            if (num - 1) not in numSet:
                # It is a part of a sequence
                length = 0
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
 