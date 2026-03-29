class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}

        for i in range(len(nums)):
            num = nums[i]
            diff = target - nums[i]
            if diff in num_index:
                return [num_index[diff], i]
            num_index[num] = i