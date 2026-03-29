class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_nums = defaultdict(int)
        res = []
        for n in nums:
            frequency_nums[n] += 1
        
        # Sort the tuples from items() by value descending
        s = sorted(frequency_nums.items(), key=lambda key: key[1], reverse=True)
        
        # Grab the k elements with highest frequency
        for i in range(k):
            res.append(s[i][0])

        return res