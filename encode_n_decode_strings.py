class Solution:
    SEPARATOR = "#"

    def encode(self, strs):
        """
        @param: strs: a list of strings
        @return: encodes a list of strings to a single string.
        """
        ans = ""
        return ans.join([f"{len(s)}{self.SEPARATOR}{s}" for s in strs])


    def decode(self, s):
        """
        @param: str: A string
        @return: decodes a single string to a list of strings
        """
        ans, i = [], 0
        while i < len(s):
            length_str = ""
            length = 0
            word = ""
            while s[i] in "0123456789":
                length_str += s[i]
                i += 1
            if s[i] == "#":
                length = int(length_str) if length_str else 0
                i += 1
            end = i + length
            while i < end:
                word += s[i]
                i += 1
            if word:
                ans.append(word)
        return ans


if __name__ == "__main__":
    strs = ["lint", "code", "love", "you"]
    s = Solution()
    encoded = s.encode(strs)
    print(encoded)
    decoded = s.decode(encoded)
    print(decoded)
    assert (s.decode(encoded) == ["lint", "code", "love", "you"])

