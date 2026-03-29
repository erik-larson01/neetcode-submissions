class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        prefix = [0] * n
        suffix = [0] * n

        # Loop from left to right
        # Prefix[i] is the product of all elements before i
        prefix[0] = 1
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        print(prefix)

        # Loop from right to left
        # Suffix[i] is the product of all elements after i
        suffix[n - 1] = 1
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        print(suffix)

        # Product except self = product before self * product after self
        for i in range(n):
            result[i] = prefix[i] * suffix[i]
        return result