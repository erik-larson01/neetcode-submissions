class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_nums = defaultdict(int)
        res = []
        for n in nums:
            frequency_nums[n] += 1
        
        result = sorted(frequency_nums.items(), key=lambda key: key[1], reverse=True)
        
        for num, frequency in result:
            if len(res) < k:
                res.append(num)

        return res