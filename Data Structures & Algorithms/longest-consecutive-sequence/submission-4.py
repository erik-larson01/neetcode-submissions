class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in nums:
            # Is it start of sequence?
            if (num - 1) not in numSet:
                # Start of sequence, start counting
                length = 0
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
