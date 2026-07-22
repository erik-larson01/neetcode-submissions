class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m

            if nums[l] <= nums[m]:
                # Left half is sorted, check if target is in left half
                if target > nums[m] or target < nums[l]:
                    # Not in left half
                    l = m + 1
                else:
                    # In left half
                    r = m - 1
            else:
                # Right half is sorted, check if target is in right half
                if target < nums[m] or target > nums[r]:
                    # Not in right half
                    r = m - 1
                else:
                    # In right half
                    l = m + 1
        return -1