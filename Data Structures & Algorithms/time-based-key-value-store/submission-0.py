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
        values = self.values.get(key)
        l,r = 0, len(self.values[key]) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res