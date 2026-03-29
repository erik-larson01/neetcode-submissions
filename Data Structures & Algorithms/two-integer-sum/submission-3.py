class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_diff = {}
        for i in range(len(nums)):
            num = nums[i]
            difference = target - num

            if difference in num_diff:
                return [num_diff[difference], i]
            else:
                num_diff[num] = i
