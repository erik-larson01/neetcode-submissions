class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        for i in range (len(nums)):
            num = nums[i]
            diff = target - num

            if diff in num_index:
                return [num_index[diff], i]
            else:
                num_index[num] = i