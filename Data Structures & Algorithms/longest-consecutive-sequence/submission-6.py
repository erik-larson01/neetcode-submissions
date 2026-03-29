class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_seq = 0;
        for n in nums:
            # Check if n is the start of a sequence
            if n - 1 not in nums_set:
                # Start of sequence
                seq = 1
                while n + 1 in nums_set:
                    seq += 1
                    n += 1
                max_seq = max(seq, max_seq)

        return max_seq