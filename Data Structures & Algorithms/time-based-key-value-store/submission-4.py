class TimeMap:

    def __init__(self):
        self.values = defaultdict(list) # Key -> List(Tuple)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Contains tuple of (value, timestamp)
        self.values[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.values and len(self.values) == 0:
            return ""
        
        res = ""
        values_list = self.values.get(key, [])
        l,r = 0, len(values_list) - 1

        # Binary search to find the result
        while l <= r:
            m = (l + r) // 2
            key_value, key_timestamp = values_list[m][0], values_list[m][1]
            # Find the rightmost value with t <= timestamp
            if key_timestamp <= timestamp:
                res = key_value
                l = m + 1
            else:
                r = m - 1
        return res