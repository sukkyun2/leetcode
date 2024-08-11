class Solution:
    def strStr(self, h: str, n: str) -> int:
        for i in range(len(h)):
            if n == h[i:i+len(n)]:
                return i

        return -1