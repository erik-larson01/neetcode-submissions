class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq = 0
        nums_set = set(nums)

        for n in nums:
            if n - 1 not in nums_set:
                seq = 1
                while n + 1 in nums_set:
                    seq += 1
                    n += 1
                max_seq = max(seq, max_seq)
        return max_seq