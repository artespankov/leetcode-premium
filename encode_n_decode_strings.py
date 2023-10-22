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
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            w = s[j + 1:j + length + 1]
            ans.append(w)
            i = j + length + 1
        return ans


if __name__ == "__main__":
    strs = ["lint", "code", "love", "you"]
    s = Solution()
    encoded = s.encode(strs)
    # print(encoded)
    # decoded = s.decode(encoded)
    # print(decoded)
    assert (s.decode(encoded) == ["lint", "code", "love", "you"])

