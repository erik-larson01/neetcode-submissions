class Solution:

    def encode(self, strs: List[str]) -> str:
        # Needs to be in format len#str
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []

        # Use two pointers to track start and end of word
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoded.append(s[i:j])
            i = j
        return decoded