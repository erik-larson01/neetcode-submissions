class Solution:

    def encode(self, strs: List[str]) -> str:
        # Add '#' as well as the length of string such as 4#neet#4code
        full_str = ""
        for string in strs:
            length = len(string)
            encoded = f'{length}#{string}'
            full_str += (encoded)
        return full_str

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1 # Find the first '#'
            # After found, slice word based on the length
            length = int(s[i:j])
            i = j + 1 # First letter
            j = i + length # last letter
            word = s[i:j]
            decoded.append(word)
            i = j # Reset i to the end
        return decoded