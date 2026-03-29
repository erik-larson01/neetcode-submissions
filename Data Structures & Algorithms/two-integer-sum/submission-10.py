class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_index = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in diff_index:
                return [diff_index[complement], i]
            diff_index[nums[i]] = i
        return []
