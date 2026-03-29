class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        pivot = -1
        # Find the pivot (smallest element)
        while l < r: # Stops when l == r
            m = (l + r) // 2
            if nums[r] < nums[m]:
                # R and M are in same group
                l = m + 1
            else:
                # L and M are in same group
                r = m
        
        pivot = l # l == r

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        # Use pivot and search in left half (sorted array)
        res = binary_search(0, pivot - 1)
        if res != -1:
            return res
        
        # Search in other half (sorted array)
        return binary_search(pivot, len(nums) - 1)

