class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_index = {} # value -> index

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in val_index:
                return [val_index[complement], i]
            val_index[nums[i]] = i
        return []
